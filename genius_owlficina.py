import machine
from machine import Pin
from machine import PWM
import time
import _thread
import os
from time import sleep
from sys import exit

#------------------------------------
# Setup dos pinos
#------------------------------------

ledAzul = Pin(2, Pin.OUT)
ledAmarelo = Pin(26, Pin.OUT)
ledVerde = Pin(13, Pin.OUT)
ledVermelho = Pin(14, Pin.OUT)

botaoAzul = Pin(4, Pin.IN)
botaoAmarelo = Pin(19, Pin.IN)
botaoVerde = Pin(18,Pin.IN)
botaoVermelho = Pin(21, Pin.IN)

beep = PWM(Pin(23), freq=262, duty=512)

#------------------------------------
# Variáveis globais
#------------------------------------

letra_para_led = {"R": ledVermelho, "G": ledVerde, "B": ledAzul, "Y": ledAmarelo}
nota_para_freq = {"do": 262, "re": 294, "mi": 330, "fa": 349}
mapa = [] # guarda a pausa, a duracao e a cor de cada nota
bpm = 0
duracao_beat = 0
margem_de_erro = 200 # milissegundos
num_da_nota = -1

#------------------------------------
# Inicialização do mapa
#------------------------------------

with open("music1.txt", "r") as file:
	for line in file:
		if num_da_nota == -1:
			bpm = int(line)
			duracao_beat = 60000 / (bpm * 4)
			num_da_nota += 1
			continue
		pausa = float(line.split(" ")[0])
		duracao = int(line.split(" ")[1])
		cor = line.split(" ")[2]
		nota = line.split(" ")[3].strip("\n")
		dic = {"pausa": pausa, "duracao": duracao, "cor": cor, "nota": nota}
		mapa.append(dic)

#------------------------------------
# Funções próprias
#------------------------------------

def checaBotao(esperado):
	apertado = ""
	if botaoVermelho.value():
		apertado = "R"
	elif botaoVerde.value():
		apertado = "G"
	elif botaoAzul.value():
		apertado = "B"
	elif botaoAmarelo.value():
		apertado = "Y"
	else:
		apertado = "nenhum"
	
	if esperado == apertado and apertado != "nenhum":
		return 0 # botao apertado foi o esperado
	elif apertado != "nenhum":
		return 1 # botao apertado foi o errado
	else:
		return 2 # nenhum botao foi apertado

def perde_e_morre():
	print("morreu")
	# faz o trompete triste e fecha o programa
	ledVermelho.value(1)
	beep.freq(200)
	sleep(0.5)
	beep.freq(160)
	sleep(1)
	beep.freq(120)
	sleep(1)
	beep.freq(1)
	ledVermelho.value(0)
	exit(0)

def tocaNota(nota, led, duracao):
	# roda em uma thread separada para não engarrafar a execução do jogo
	led.value(1)
	beep.freq(nota_para_freq[nota])
	sleep(duracao)
	beep.freq(1)
	led.value(0)

def pisca_tudo(n):
	for i in range(5):
		ledAzul.value(1)
		sleep(0.2)
		ledAzul.value(0)
		ledVerde.value(1)
		sleep(0.2)
		ledVerde.value(0)
		ledAmarelo.value(1)
		sleep(0.2)
		ledAmarelo.value(0)
		ledVermelho.value(1)
		sleep(0.2)
		ledVermelho.value(0)

def ganha_jogo_ebaaa():
	# toca uma musiquinha de vitória e pisca todos os leds
	thread_piscante = _thread.start_new_thread(pisca_tudo, (2))

def range_custom(n):
	m = [0]
	for i in range(1, n + 1):
		m.append(i)
	return m

#------------------------------------
# Loop do jogo
#------------------------------------

gameOver = False
lastStep = len(mapa)
step = 1
lastClickTime = 0

while not gameOver:
	while step <= lastStep:
		for j in range(step):
			# tocando a musiquinha pro usuário
			print("maconha")
			sleep(mapa[j]["pausa"])
			letra_para_led[mapa[j]["cor"]].value(1)
			beep.freq(nota_para_freq[mapa[j].get("nota")])
			sleep(mapa[j]["duracao"])
			beep.freq(1)
			letra_para_led[mapa[j]["cor"]].value(0)

		botoes_apertados = 1
		step_bem_sucedido = False
		while botoes_apertados <= step:
			nota_atual = mapa[botoes_apertados]
			
			resultado = checaBotao(nota_atual["cor"])
			# checa se algum botão foi apertado e se foi o certo
			if resultado == 2:
				# nenhum botão foi apertado, reinicia o loop
				continue
			if resultado == 1:
				# o botão errado foi apertado, mata o jogador
				print("Tu apertou a corzinha errada :^(")
				step_bem_sucedido = False
				break

			if resultado == 0:
				# mutex.acquire()
				# o botão certo foi apertado
				if botoes_apertados == 1:
					# seta o tempo do último click para o tempo do primeiro click
					lastClickTime = int(time.time() * 1000)
					# pisca o led e grita o buzzer de acordo com a nota atual
					if step == 1:
						_thread.start_new_thread(tocaNota, (nota_atual["nota"], letra_para_led[nota_atual["cor"]], nota_atual["duracao"]))
						step_bem_sucedido = True
					else:
						_thread.start_new_thread(tocaNota, (nota_atual["nota"], letra_para_led[nota_atual["cor"]], nota_atual["duracao"]))  
					botoes_apertados += 1
				else:
					# calcula o tempo decorrido desde o último click
					t = int(time.time() * 1000)
					dt = t - lastClickTime
					lastClickTime = t
					# compara com o tempo necessário para um acerto
					tempo_perfeito = nota_atual["pausa"] * duracao_beat + mapa[botoes_apertados - 1]["duracao"] * duracao_beat
					if botoes_apertados == step:
						step_bem_sucedido = True
					if(dt > tempo_perfeito - margem_de_erro and dt < tempo_perfeito + margem_de_erro):
						_thread.start_new_thread(tocaNota, (nota_atual["nota"], letra_para_led[nota_atual["cor"]], nota_atual["duracao"]))
						botoes_apertados += 1
						if botoes_apertados == step:
							step_bem_sucedido = True
					else:
						print("Tu não apertou no ritmo :^(")
						break

		# o jogador falhou nesse passo de alguma forma
		if not step_bem_sucedido:
			perde_e_morre()
		# o jogador é foda
		step += 1

	# se a execução chegou até aqui, o jogador venceu
	ganha_jogo_ebaaa()
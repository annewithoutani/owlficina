<p align="center">
  <img src="https://i.imgur.com/CNzb2O9.png" width="300" /><br/>
Genio só que melhor e com ritmo (se funcionasse) <br/>
</p>

<br/>

## :pushpin: Descrição

A ideia do projeto consiste em criar um jogo semelhante ao "Genius", que se baseia na memorização e repetição de uma determinada ordem de cores, mas com a adição de uma mecânica ritmica de modo que o jogador precise não somente memorizar a ordem das cores, mas o ritmo em que cada nota toca.

<br/>

## :robot: Montagem do dispositivo físico

### Lista de materiais

| Quantidade | Nome | Link para referência |
| --- | --- | --- |
| 1 | ESP32 e Cabo USB | https://www.makerhero.com/produto/modulo-wifi-esp32s-nodemcu-esp-12/ |
| 4 | Chave Táctil Push-Button | https://www.makerhero.com/produto/chave-tactil-push-button/ |
| 1 | Led Vermelho | https://www.makerhero.com/produto/led-difuso-5mm-vermelho/ |
| 1 | Led Verde | https://www.makerhero.com/produto/led-difuso-5mm-verde/ |
| 1 | Led Amarelo | https://www.makerhero.com/produto/led-difuso-5mm-amarelo/ |
| X | Jumpers Macho-Macho | https://www.makerhero.com/produto/jumpers-macho-macho-x40-unidades/ |
| 3 | Mini Protoboard | https://www.makerhero.com/produto/mini-protoboard-170-pontos/ |
| 4 | Resistor 1K ohms | https://www.makerhero.com/produto/resistor-1k%cf%89-1-4w/ |
| 2 | Resistor 220 ohms | https://www.makerhero.com/produto/resistor-270%cf%89-1-4w/ |
| 2 | Resistor 270 ohms | https://www.makerhero.com/produto/resistor-220%CF%89-1-4w/ |
| 2 | Buzzer Passivo | https://www.saravati.com.br/buzzer-9mm-5v-passivo.html?gad_source=4&gclid=CjwKCAiAxea5BhBeEiwAh4t5K0zKPGQdOFeyNEBHyCtRAK0zN6LkCiApWqqqz0_YejuaAufx_H1gqxoCvusQAvD_BwE |
| 1 | Fonte de alimentação | (Conectamos com o computador) |

### Lista de conexões

| Componente | Pino da placa |
| --- | --- |
| Led Azul (Integrado à placa) | 2 |
| Led Amarelo| 26 |
| Led Verde | 13 |
| Led Vermelho | 14 |
| Push Button A | 4 |
| Push Button B | 19 |
| Push Button C | 18 |
| Push Button D | 21 |
| Buzzer | 23 |


### Funcionamento dos sensores e atuadores

#### :metal: Sensores

##### Chave Táctil Push-Button

A Chave Táctil ou Push Buttom como também é conhecida é um dos componentes eletrônicos mais utilizados para prototipagem de projetos.

(Especificação técnica: https://cromatek.com.br/datasheet/componentes-diversos/chave-tactil-180-graus-4mm.pdf)

Esta chave é um tipo de interruptor pulsador (conduz somente quando pressionado), dessa forma ao ser pressionado ele abre ou fecha os contatos do dispositivo, conectando dois pontos em um circuito. As principais características da chave que utilizamos são: 
– Dimensões: 6x6x5mm;
– Espaço entre terminais: 5mm;
– Terminais: 4;
– Tensão Máxima: 12V;
– Corrente Máxima: 0,5A.

#### :gun: Atuadores

##### LEDs

O LED é um componente eletrônico semicondutor muito utilizado em projetos e circuitos eletrônicos para sinalização visual. Pode ser utilizado facilmente em protoboards ou placas de circuito impresso.

(Especificação técnica: http://www.symtronic.com.br/produtos/arquivos/SYM-R503-30-D_8206.pdf)

Os LEDs (Light Emitting Diode) são diodos com capacidade de emitir luz quando polarizados diretamente. Eles permitem passagem de corrente em apenas um sentido, circulando sempre do terminal denominado ânodo (positivo) para o terminal cátodo (negativo). É necessário observar a corrente e a tensão direta do LED na hora de utilizá-lo no circuito, sendo indicado uso de resistores para limitar a corrente. 

Cada cor de LED tem algumas especificidades diferentes. Suas principais características são, por cor: 

###### Vermelho
- Tamanho: 5mm;
- Tensão: 2,0 a 2,21V;
- Corrente: 25mA;
- Intensidade luminosa: 1000mCD (milicandela);
- Vida útil: 50,000 Horas;
- Ângulo de abertura: 120° graus.

###### Amarelo
- Tamanho: 5mm;
- Tensão: 2,0 a 2,21V;
- Corrente: 20mA;
- Intensidade luminosa: 1000mCD (milicandela);
- Vida útil: 50,000 Horas;
- Ângulo de abertura: 120° graus.

###### Verde
- Tamanho: 5mm;
- Tensão: 1,9 a 2,21V;
- Corrente: 20mA;
- Intensidade luminosa: 800 a 1000mCD (milicandela);
- Vida útil: 50,000 Horas;
- Ângulo de abertura: 120º graus.

##### Buzzer Passivo

O buzzer, também conhecido como beeper, é um dispositivo emissor de som encontrado nos mais diversos tamanhos e formatos. 

(Especificação técnica: https://www.addicore.com/products/passive-buzzer?srsltid=AfmBOorEXIwlxfsv40y50I5qrcMyselRnIbGxTBraRW1il2OzgowxXo7)

Quando uma tensão é aplicada nos eletrodos, o disco é deformado fazendo com que ele se movimente dentro do buzzer e gere som. Este tipo de buzzer foi criado para proporcionar um controle mais preciso do som para reprodução de notas musicais e criação de melodias.

As principais características do buzzer que utilizamos são: 
- Varia a frequência de emissão;
- Funciona como um pequeno alto-falante;
- Tensão de operação: 4 a 8V;
- Tensão recomendada: 5V;
- Corrente máxima: 40mA;
- Diâmetro: 12mm;
- Altura: 8,5mm;

### Circuito

<p align="center">
Figura - Diagrama do circuito (nn temos?)<br/>
  <img src="https://i.imgur.com/GniJVDn.jpg" width="400" /><br/>
</p>
Informações importantes sobre o circuito, onde colocá-lo, entre outros.
<br/>

<br/>

## :electric_plug: Funcionamento do sistema

O sistema supostamente é um jogo Genius com elementos de musicalidade e ritmo para diferencia-lo. Ele funciona(ria) da seguinte maneira:

1. Define-se uma sequência de notas musicais, suas durações e a cor de led que deve piscar com essa nota.
2. Um número X (inicialmente 1) de notas são tocadas (com o buzzer) e seus leds correspondentes brilham pela duração da nota
3. O input do jogador - via botões - é lido.
4. Se o jogador conseguir clicar na sequência certa de botões no ritmo da música, ele avança para o próximo passo (X += 1). Se não, o jogo acaba.
5. Se o passo atual era o último passo, o jogador vence o jogo.
6. Volta para o passo 2.

Nosso código começa com a importação dos módulos usados e o setup dos pinos:

``` Python
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
```

depois, declaramos algumas variáveis globais importantes que serão usadas no resto do programa:

``` Python
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

```

Então, lemos um arquivo que contém a sequência de notas, durações e cores de led e inicializa nosso mapa/nível com as informações desse arquivo:

``` Python
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
```

O formato desses arquivos de nível é o seguinte, eles começam com o BPM da música, e cada linha subsequente é composta de 4 valores: a pausa em segundos entre última nota e a atual, a duração da nota atual, a letra correspondente à cor do led e a nota que deve ser tocada pelo buzzer. Ex:

```
120
0.5 2 R do
0.2 1 R do
0.2 1 R do
0.2 1 G re
0.5 2 R do
0.5 2 Y mi
0.2 2 B fa
```

Depois, declaramos nossas funções auxiliares que serão usadas no loop principal do jogo:

``` Python
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
```

E por fim, temos o loop principal do jogo, com a participação especial do código mais bagunçado que você já viu na vida (devido ao método Extreme Go Horse que usamos no processo de correção de bugs):

``` Python
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
```

<br/>

## :busts_in_silhouette: Contribuir no projeto

### Features implementadas

- [x] Tocar música
- [x] Ler inputs
- [x] Piscar LEDs no ritmo da música
- [x] Sabe quando o jogador perde (de vez em quando)
- [ ] Correção de bugs
- [ ] Fazer o jogo funcionar
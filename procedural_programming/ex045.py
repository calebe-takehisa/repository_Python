"""
Crie um programa que faça o computador jogar Jokenpô com você.
SAÍDA
Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada?
JO (delay 1)
KEN (delay 1)
PO!!! (delay 1)
-=-=-=-=-=-=-=-=-=-=-=-=
Computador jogou XXXXXX
Jogador jogou YYYYYY
-=-=-=-=-=-=-=-=-=-=-=-=
VITORIA / DERROTA / EMPATE

"""
import time
import random


def tempo(texto):
    time.sleep(0.5)
    print(texto)


vitoria = 0
derrota = 0
empate = 0
while True:
    computador = random.randint(0, 2)
    if computador == 0:
        jogada_computador = 'Pedra'
    elif computador == 1:
        jogada_computador = 'Papel'
    else:
        jogada_computador = 'Tesoura'

    while True:
        try:
            print('Suas opções:\n'
                  '[ 0 ] PEDRA\n'
                  '[ 1 ] PAPEL\n'
                  '[ 2 ] TESOURA')
            player = int(input('Qual é a sua jogada? '))
            if player == 0:
                jogada_player = 'Pedra'
                break
            elif player == 1:
                jogada_player = 'Papel'
                break
            elif player == 2:
                jogada_player = 'Tesoura'
                break
            else:
                print('Escolha apenas jogadas válidas\n')
        except:
            print('Escolha apenas jogadas válidas\n')
    print('JO')
    tempo('KEN')
    tempo('PO!!!')
    tempo('-=' * 12)
    print(f'Computador jogou {jogada_computador}')
    print(f'Jogador jogou {jogada_player}')
    print('-=' * 12)
    if player == computador:
        print('EMPATE\n')
        empate += 1
    elif player == 0 and computador == 1 or player == 1 and computador == 2 or player == 2 and computador == 0:
        print('DERROTA\n')
        derrota += 1
    else:
        print('VITÓRIA\n')
        vitoria += 1
    print(f'Vitórias:[{vitoria}] Derrotas:[{derrota}] Empates:[{empate}]\n')

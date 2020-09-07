"""
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o
jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

SAÍDA:
Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?
Qual é seu palpite? X
Mais... Tente mais uma vez.
Qual é seu palpite? Y
Menos... Tente mais uma vez.
Qual é seu palpite? Z
Acertou com 3 tentativas. Parabéns!

"""
from random import randint
from time import sleep

numero_secreto = randint(0, 10)

print('Sou seu computador...')
sleep(0.5)
print('Acabei de pensar em um número entre 0 e 10.')
sleep(0.5)
print('Será que você consegue adivinhar qual foi?')
sleep(0.8)

tentativas = 0
while True:
    try:
        palpite = int(input('Qual é seu palpite? '))
        if palpite == numero_secreto:
            tentativas += 1
            break
        elif palpite > numero_secreto:
            print('Menos... Tente mais uma vez.')
            tentativas += 1
            continue
        else:
            print('Mais... Tente mais uma vez.')
            tentativas += 1
            continue
    except:
        print('Digite apenas números inteiros.')

print(f'Acertou com {tentativas} tentativas. Parabéns!')

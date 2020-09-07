"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá
escrever na tela se o usuário venceu ou perdeu.
SAÍDA:
Vou pensar em um número entre 0 e 5. Tente adivinhar...
Em que número eu pensei? x
Processando...

True:
Parabéns! Você conseguiu me vencer!

False:
Ganhei! Eu pensei no número 0 e não no 3!

"""
# Minha solução:

import random
from time import sleep
num_pc = random.randint(0, 5)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
num_usuario = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(1)
if num_usuario == num_pc:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print(f'Ganhei! Eu pensei no número {num_pc} e não no {num_usuario}!')
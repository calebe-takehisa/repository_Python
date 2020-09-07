"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
SAÍDA:
Digite um número: 10
[1] [2] 3 4 [5] 6 7 8 9 [10]
O número 10 foi divisível 4 vezes
E por isso ele NÃO É PRIMO!

Digite um número: 13
[1] 2 3 4 5 6 7 8 9 10 11 12 [13]
O número 13 foi divisível 2 vezes
E por isso ele É PRIMO!
"""
n = int(input('Digite um número: '))

div = 0
for x in range(1, n + 1):
    if n % x == 0:
        print(f'\033[34m{x}\033[m', end=' ')
        div += 1
    else:
        print(f'\033[31m{x}\033[m', end=' ')

if div <= 2:
    print(f'\nO número {n} foi divisível {div} vezes')
    print('E por isso ele É PRIMO!')
else:
    print(f'\nO número {n} foi divisível {div} vezes')
    print('E por isso ele NÃO É PRIMO!')

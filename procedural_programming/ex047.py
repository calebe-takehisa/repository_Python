"""
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
SAÍDA:
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 Acabou
"""

for num in range(1, 51):
    if num % 2 == 0:
        print(num, end=' ')
    if num == 50:
        print('Acabou', end=' ')

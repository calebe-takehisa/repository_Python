"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.

SAÍDA:
========================================
10 Termos de uma  Progressão Aritmética
========================================
Primeiro termo: 0
Razão: 2
0 → 2 → 4 → 6 → 8 → 10 → 12 → 14 → 16 → 18 → ACABOU
"""

print('='*40)
print('10 Termos de uma  Progressão Aritmética')
print('='*40)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

contador = 0
while contador < 10:
    print(f'{primeiro_termo}', end=' → ')
    primeiro_termo += razao
    contador += 1

print('ACABOU')
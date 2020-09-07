"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome.
SAÍDA:
Qual é seu nome completo? Mario da Silva Mendonça
Seu nome tem Silva? True

"""

# Minha solução 1:
nome = input('Qual é seu nome completo? ').lower().split()
check = 'silva' in nome
print(f'Seu nome tem Silva? {check}')
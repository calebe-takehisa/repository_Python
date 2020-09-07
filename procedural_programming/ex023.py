"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
SAÍDA:
Informe um número: 3234
Analisando o número 3234
Unidade: 4
Dezena: 3
Centena: 2
Milhar: 3

"""

# Minha solução 1:
num = int(input('Informe um número: '))
print(f'Analisando o número {num}')
unidade = num % 10
dezena = num % 100 // 10
centena = num % 1000 // 100
milhar = num % 10000 // 1000
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
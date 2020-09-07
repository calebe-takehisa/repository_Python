"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
"""
x = 0
soma_par = 0

while x < 6:
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma_par = n + soma_par
    x += 1

print(f'A soma de todos os pares é {soma_par}.')
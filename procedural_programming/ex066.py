"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).

SAÍDA:
Digite um valor (999 para parar): 3
Digite um valor (999 para parar): 8
Digite um valor (999 para parar): 1
Digite um valor (999 para parar): 7
Digite um valor (999 para parar): 999
A soma dos 4 valores foi 19!
"""

number = total = elements = 0
while number != 999:
    number = int(input('Digite um valor (999 para parar): '))
    if number != 999:
        total += number
        elements += 1

print(f'A soma dos {elements} valores foi {total}!')
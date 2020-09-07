"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).

SAÍDA:
Digite um número [999 para parar]: 8
Digite um número [999 para parar]: 2
Digite um número [999 para parar]: 1
Digite um número [999 para parar]: 7
Digite um número [999 para parar]: 999
Você digitou 4 números e a soma entre eles foi 18.

"""
number = 0
total_number = 0
amount = 0

while number != 999:
    number = int(input('Digite um número [999 para parar]: '))
    if number != 999:
        total_number += 1
        amount += number
    else:
        break

print(f'Você digitou {total_number} números e a soma entre eles foi {amount}.')
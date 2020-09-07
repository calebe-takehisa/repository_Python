"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a
digitar valores.

SAÍDA:
Digite um número:
Quer continuar [S/N] ?
Você digitou X números e a média foi Y.YY
O maior valor foi M e o menor foi N

"""

numeros = []
total = 0
elementos = 0

while True:
    try:
        numero = int(input('Digite um número: '))
        total += numero
        elementos += 1
        numeros.append(numero)
        continua = input('Quer continuar [S/N]? ').lower()
        if continua == 's':
            continue
        elif continua == 'n':
            break
        else:
            print('Digite opções válidas')
    except ValueError:
        print('Valor inválido')

media = total / elementos

print(f'Você digitou {elementos} números e a média foi {media}')
print(f'O maior valor foi {max(numeros)} e o menor foi {min(numeros)}')

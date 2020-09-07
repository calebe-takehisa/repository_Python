"""
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
SAÍDA:
Me diga um número qualquer: x
PAR:
O número x é PAR
IMPAR:
O número x é ÍMPAR
"""
# Minha solução:
num = int(input('Me diga um número qualquer: '))
check = num % 2
if check == 0:
    print(f'O número {num} é PAR')
else:
    print(f'O número {num} é ÍMPAR')
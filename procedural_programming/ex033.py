"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menos.
SAÍDA:
Primeiro valor: 7
Segundo valor: 2
Terceiro valor: 4
O menor valor digitado foi 2
O maior valor digitado foi 7

ATT¹: O programa não está aceitando números negativos.

"""
# Minha solução:
def leiaint(num):
    try:
        if num.isdigit():
            num = int(num)
            return num
        elif num == 'x':
            return 'x'
        else:
            print('Digite um número válido')
            return 1
    except:
        pass

num = input('Digite um número ou digite "x" para sair: ')
num = leiaint(num)
maior = num
menor = num
while num != 'x':
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    num = input('Digite um número ou digite "x" para sair: ')
    num = leiaint(num)


print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
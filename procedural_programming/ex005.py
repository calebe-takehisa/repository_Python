"""
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

SAÍDA:
Digite um número: 2
Analisando o valor 2, seu antecessor é 1 e o sucessor é 3.
"""
# Minha solução:
num = int(input('Digite um número: '))
print(f'Analisando o valor {num}, seu antecessor é {num-1} e o sucessor é {num+1}.')

# Solução do Professor:
n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}.'.format(n, a, s))
#ou
m = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}.'.format(m, (m-1), (m+1)))
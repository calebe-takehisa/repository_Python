"""
Faça um programa que leia um número inteiro qualquer e mostre na tela
a sua tabuada.

SAÍDA:
Digite um número para ver sua tabuada: N
____________
N x 1  = R
N x 2  = R
N x 3  = R
N x 4  = R
N x 5  = R
N x 6  = R
N x 7  = R
N x 8  = R
N x 9  = R
N x 10 = R
____________

"""
# Minha solução:
n = int(input('Digite um número para ver sua tabuada:'))
print("_"*14)
for x in range(1, 11):
    print(f'{n} x {(x):2} = {n*x}')
print("_"*14)

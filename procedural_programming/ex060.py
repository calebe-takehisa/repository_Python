"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
SAÍDA:
Digite um número para calcular seu fatorial: 6
Calculando 6! = 6 x 5 x 4 x 3 x 2 x 1 = 720
"""


def numint(n):
    try:
        n = int(n)
        return n
    except:
        return


n = numint(input('Digite um número para calcular seu fatorial: '))

lista = [n]
fatorial = n
for numeros in range(n-1, 0, -1):
    fatorial *= numeros
    lista.append(numeros)


print(fatorial)
print(lista, sep=' x ')


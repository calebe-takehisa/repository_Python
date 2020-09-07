"""
Crie um algoritmo que leia um númeor e mostre o seu dobro, triplo e raiz quadrada.

SAÍDA:
Digite um número: x
O dobro de x vale y.
O triplo de x vale z.
A raiz quadrada de x é igual a n.nn.

"""
# Minha solução:
import math
nun = int(input('Digite um número: '))
print(f'O dobro de {num} vale {num*2}.')
print(f'O triplo de {num} vale {num*3}.')
print('A raiz quadrada de {} é igual a {:.2f}.'.format(num, math.sqrt(num)))

# Solução do Professor:
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))
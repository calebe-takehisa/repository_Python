"""
Crie um programa que leia dois números e mostre a soma entre eles.

SAÍDA:
Digite um valor: x
Digite outro valor: y
A soma entre x e y é igual a z!
"""
# Minha solução:
num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite outro número: '))

print(f'A soma de {num_1} e {num_2} é igual a {num_1+num_2}!')

# Solução do Professor:
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print('A soma entre {} e {} é igual a {}!'.format(n1, n2, s))
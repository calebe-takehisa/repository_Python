"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa.

SAÍDA:
Comprimento do cateto oposto: 3.5
Comprimento do cateto adjacente: 4.75
A hipotenusa vai medir 5.90

"""
# Minha solução 1:
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')



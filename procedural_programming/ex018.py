"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse ângulo.

SAÍDA:
Digite o ângulo que você deseja: 30
O ângulo de 30.0 tem o SENO de 0.50
O ângulo de 30.0 tem o COSSENO de 0.87
O ângulo de 30.0 tem o TANGENTE  de 0.58
"""
# Minha solução 1:
from math import sin, cos, tan, radians
numero = int(input('Digite o ângulo que você deseja: '))

print(f'O ângulo de {numero} tem o SENO de {sin(radians(numero)):.2f}')
print(f'O ângulo de {numero} tem o COSSENO de {cos(radians(numero)):.2f}')
print(f'O ângulo de {numero} tem o TANGENTE  de {tan(radians(numero)):.2f}')
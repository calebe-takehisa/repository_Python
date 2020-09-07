"""
Escreva um programa que converta uma temperatura digitada em °C e converta para °F

SAÍDA:
Informe a temperatura em °C: 31.5
A temperatura de 31.5°C corresponde a 88.7°F
"""
# Minha solução:
celsius = input('Informe a temperatura em °C: ')
fahrenheit = (float(celsius) * (9 / 5)) + 32
print(f'A temperatura de {float(celsius):.1f}°C corresponde a {fahrenheit:.1f}°F')
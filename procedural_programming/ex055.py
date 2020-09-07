"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
SAÍDA:
Peso da 1° pessoa: 85.6
Peso da 2° pessoa: 90.2
Peso da 3° pessoa: 48.9
Peso da 4° pessoa: 70.7
Peso da 5° pessoa: 65.5
O maior peso lido foi de 90.2Kg
O menor peso lido foi de 48.9Kg

"""

pesos = []

for pessoas in range(1, 6):
    y = float(input(f'Peso da {pessoas}° pessoa: '))
    pesos.append(y)

maior_peso = max(pesos)
menor_peso = min(pesos)

print(f'O maior peso lido foi de {maior_peso:.2f}Kg')
print(f'O menor peso lido foi de {menor_peso:.2f}Kg')

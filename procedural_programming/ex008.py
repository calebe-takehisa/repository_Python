"""
Escreva um programa que leia um valor em metros e o exiba
convertido em centímetros e milímetros.

SAÍDA:
Uma distância em metros: X
A medida de X.Xm corresponde a:
X.XXXkm
X.XXhm
X.Xdam
XXdm
XXXcm
XXXXmm
"""
# Minha solução:
m = float(input('Uma distância em metros: '))
print(f'A medida de {m}m corresponde a:')
print(f'{m / 1000}km')
print(f'{m / 100}hm')
print(f'{m / 10}dam')
print(f'{int(m * 10)}dm')
print(f'{int(m * 100)}cm')
print(f'{int(m * 1000)}mm')





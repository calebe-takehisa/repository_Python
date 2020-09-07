"""
Crie um programa que leia quanto dinheiro uma pessoa em na carteira e mostre quantos dólares ela pode comprar.
Considere US$ 1,00 = R$ 3,27

SAÍDA:
Quanto dinheiro você tem na carteira? R$xx.xx
Com RSxx.xx você pode comprar US$YY.YY
"""
# Minha solução:
real = input('Quanto dinheiro você tem na carteira? R$')
dolar = float(real) / 3.27
print(f'Com RS{real} você pode comprar US${dolar:.2f}')


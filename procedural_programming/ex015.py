"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

SAÍDA:
Quantos dias Alugados? 8
Quantos Km rodados? 720
O total a pagar é de R$588.0
"""
# Minha solução:
dias_alugados = int(input('Quantos dias Alugados? '))
km_rodado = float(input('Quantos Km rodados? '))
total = (dias_alugados * 60) + (km_rodado * 0.15)
print(f'O total a pagar é de R${total:.2f}')
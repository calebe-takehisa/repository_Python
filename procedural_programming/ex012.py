"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

SAÍDA:
Qual é o preço do produto? R$XX.XX
O produto que custava R$XX.XX, na promoção com desconto de 5% vai custar R$YY.YY
"""
# Minha solução:
preco = float(input('Qual é o preço do produto? R$'))
desconto = 5
preco_com_desconto = preco-(desconto/100)*preco
print(f'O produto que custava R${preco}, na promoção com desconto de {str(desconto)}% vai custar R${preco_com_desconto:.2f}')
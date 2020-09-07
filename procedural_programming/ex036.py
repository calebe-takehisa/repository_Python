"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
o sálario do comprador e em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.
SAÍDA:
Valor da casa: R$xxxxx.xx
Salário do comprador: R$XXXX.XX
Quantos anos de financiamento? y
Para pagar uma casa de R$xxxxx.xx em y anos a prestação será de R$xxx.xx
Empréstimo NEGADO!
Empréstimo pode ser CONCEDIDO!

"""
# Minha solução:
imovel = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
financiamento = int(input('Quantos anos de financiamento? '))*12
prestacao = imovel / financiamento
print(f'Para pagar uma casa de R${imovel:.2f} em {financiamento:.0f} meses a prestação será de R${prestacao:.2f}')
if prestacao > (salario*0.30):
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')
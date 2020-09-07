"""
Desenvolva um programa que pergunta a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens mais longas.
SAÍDA:
Qual é a distância da sua viagem? 210
Você está prestes a começar uma viagem de 210.0Km.
E o Preço da sua passagem será de R$94.50

"""
# Minha solução:
viagem = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {viagem}Km.')
if viagem <= 200:
    preco = viagem * 0.50
    print(f'E o Preço da sua passagem será de R${preco:.2f}')
else:
    preco = viagem * 0.45
    print(f'E o Preço da sua passagem será de R${preco:.2f}')

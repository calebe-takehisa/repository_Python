"""
Crie um progrma que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas e  minúsculas.
Quantas letras ao tdo (sem considerar espaços).
Quantas letras tem o primeiro nome.

SAÍDA:
Digite seu nome completo: José Calebe de França Takehisa
Analisando seu nome...
Seu nome em maiúsculas é JOSÉ CALEBE DE FRANÇA TAKEHISA
Seu nome em minúsculas é josé calebe de frança takehisa
Seu nome tem ao tdo xx letras
Seu primeiro nome é José e ele tem x letras
"""

# Minha solução 1:
nome = input('Digite seu nome completo: ')
nome_format = nome.split(' ')
nome_espaco = len(nome) - nome.count(' ')

print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {nome_espaco} letras ')
print(f'Seu primeiro nome é {nome_format[0]} e ele tem {len(nome_format[0])} letras')


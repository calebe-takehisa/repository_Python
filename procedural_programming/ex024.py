"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
SAÍDA:
Em que cidade você nasceu?   SaNto Inácio
True
Em que cidade você nasceu? São Paulo
False
"""

# Minha solução 1:
cidade = input('Em que cidade você nasceu? ')
cidade = cidade.lower()
cidade = cidade.split()
cidade = cidade[0] == 'santo'
print(cidade)

# Minha solução 2:
cidade = input('Em que cidade você nasceu? ').lower().split()
cidade = cidade[0] == 'santo'
print(cidade)

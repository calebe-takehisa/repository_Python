"""
Faça um programa que leia o nome de uma pessoa e mostre um mensagem de boas-vindas.

SAÍDA:
Digite seu nome: Calebe
É um prazer te conhecer, Calebe!

"""
# Minha solução:
nome = input('Digite seu nome: ')
print(f'É um prazer te conhecer, {nome}!')

# Solução do Professor:
nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}!'.format(nome))
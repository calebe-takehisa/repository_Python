"""
Faça um programa que leia o nome completo de uma pessoa.
mostrando em seguida o primeiro e o último nome separadamente.
SAÍDA:
Digite seu nome completo: José Calebe de França Takehisa
Muito prazer em te conhecer!
Seu primeiro nome é José
Seu último nome é Takehisa

"""
# Minha solução:
nome = input('Digite seu nome completo: ').split()

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[-1]}')
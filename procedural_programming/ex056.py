"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
→ A média de idade do grupo.
→ Qual é o nome do homem mais velho.
→ Quantas mulheres têm menos de 20 anos.

SAÍDA:
----- 1° PESSOA -----
Nome: João
Idade: 22
Sexo [M/F]: M
----- 2° PESSOA -----
Nome: Maria
Idade: 12
Sexo [M/F]: F
----- 3° PESSOA -----
Nome: Cláudio
Idade: 75
Sexo [M/F]: M
----- 4° PESSOA -----
Nome: Ana
Idade: 9
Sexo [M/F]: F
A média de idade do grupo é de 29.5 anos.
O homem mais velho tem 75 anos e se chama Cláudio.
Ao todo são 2 mulheres com menos de 20 anos.

"""
total_idades = 0
idade_h_velho = 0
nome_h_velho = 0
mulheres_menos_vinte = 0

for pessoa in range(1, 5):
    print(f'----- {pessoa}° PESSOA - ----')
    nome = input('Nome: ').lower().capitalize()
    while True:
        try:
            idade = int(input('Idade: '))
            break
        except:
            print('Digite uma idade válida!')
    while True:
        sexo = input('Sexo[M/F]: ').upper()
        if sexo == 'M' or sexo == 'F':
            break
        else:
            print('Digite uma das opções indicadas!')
    total_idades += idade
    if sexo == 'M':
        if idade >= idade_h_velho:
            idade_h_velho = idade
            nome_h_velho = nome
    if sexo == 'F':
        if idade < 20:
            mulheres_menos_vinte += 1

media_idade = total_idades / 4

print(f'\nA média de idade do grupo é de {media_idade} anos.')

if nome_h_velho == 0:
    print(f'Não foram cadastrados homens no grupo.')
else:
    print(f'O homem mais velho tem {idade_h_velho} anos e se chama {nome_h_velho}.')

print(f'Ao todo são {mulheres_menos_vinte} mulheres com menos de 20 anos.')

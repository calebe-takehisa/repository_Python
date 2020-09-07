"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o pragrama deverá perguntar se
o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.

SAÍDA:
---------------------------
    CADASTRE UMA PESSOA
---------------------------
Idade: 22
Sexo: [M/F] M
---------------------------
Quer continuar? [S/N] s
---------------------------
    CADASTRE UMA PESSOA
---------------------------
Idade: 85
Sexo: [M/F] F
---------------------------
Quer continuar? [S/N] n
Total de pessoas com mais de 18 anos: 2
Ao todo temos 1 homens cadastrados
E temos 0 mulheres com menos de 20 anos
"""

older_eighteen = man_register = women_under_twenty = 0
continue_while = True
while continue_while:
    print('-' * 27)
    print('CADASTRE UMA PESSOA')
    print('-' * 27)
    age = int(input('Idade: '))
    sex = input('Sexo: [M/F] ').lower()
    if age > 17:
        older_eighteen += 1
    if sex == 'm':
        man_register += 1
    if sex == 'f':
        if age < 20:
            women_under_twenty += 1
    print('-' * 27)
    while_continue = input('Quer continuar? [S/N] ').lower()
    if while_continue == 's':
        continue
    elif while_continue == 'n':
        continue_while = False

print(f'Total de pessoas com mais de 18 anos: {older_eighteen}')
print(f'Ao todo temos {man_register} homens cadastrados')
print(f'E temos {women_under_twenty} mulheres com menos de 20 anos')

"""
A confederação Nacional de Ntação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
-Até 9 anos:MIRIM
-Até 14 anos:INFANTIL
-Até 19 anos:JUNIOR
-Até 25 anos:SÊNIOR
-Acima:MASTER

SAÍDA:
Ano de Nascimento: xxxx
O atleta tem yy anos.
Classificação: zzzzz
"""
from datetime import datetime
ano_atual = datetime.now().year

while True:
    try:
        data_nascimento = input('Ano de Nascimento: ')
        idade = ano_atual - int(data_nascimento)
        if int(data_nascimento) >= 1903:
            print(f'O atleta tem {idade} anos.')
            if idade < 0:
                print('Idade considerada inválida')
            elif idade <= 9:
                print('Classificação: MIRIM')
                break
            elif idade <= 14:
                print('Classificação: INFANTIL')
                break
            elif idade <= 19:
                print('Classificação: JUNIOR')
                break
            elif idade <= 25:
                print('Classificação: SÊNIOR')
                break
            elif idade > 25:
                print('Classificação: MASTER')
                break
        else:
            print('Digite apenas anos válidos (A pessoa mais velho no mundo atualmente nasceu em 1903)')
    except:
        print('Digite apenas anos válidos')

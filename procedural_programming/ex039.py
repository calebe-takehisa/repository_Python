"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
se ele ainda vai se alistar ao serviço
militar, se é a hora de se alistar ou se já passou do tempo do alistamento.
Seu programa tambem deverá mostrar o tempo que falta ou que
passou do prazo.
SAÍDA:
Ano de nascimento:XXXX
Quem nasceu em XXXX tem YY anos em 2020.

falta:
Ainda faltam Z anos para o alistamento
Seu alistamento será em XXXX

imediato:
Você tem que se alistar IMEDIATAMENTE!

passou:
Você já deveria ter se alistado há X anos.
Seu alistamento foi em XXXX

"""
# Minha solução:
from datetime import datetime

ano = datetime.now().year

while True:
    try:
        nascimento = input('Ano de nascimento: ')
        if len(nascimento) == 4:
            nascimento = int(nascimento)
            idade = ano - nascimento
            print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano}.')
            if idade == 18:
                print('Você tem que se alistar IMEDIATAMENTE!\n')
            elif idade < 18:
                print(f'Ainda faltam {18 - idade} anos para o alistamento.')
                print(f'Seu alistamento será em {(18 - idade) + ano}.\n')
            else:
                print(f'Você já deveria ter se alistado há {(idade - 18)} anos.')
                print(f'Seu alistamento foi em {ano - (idade - 18)}.\n')
        else:
            print('Digite um ano de nascimento válido.\n')
    except:
        print('Digite um ano de nascimento válido.')
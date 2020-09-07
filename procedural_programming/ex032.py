"""
Faça um programa que leia um ano qualquer e mostre se ele é Bissexto.

SAÍDA:
Que ano quer analisar? Coloque 0 para nalisar o ano atual:
Não é Bissexto:
O ano xxxx NÃO é bissexto.
É Bissexto:
O ano xxxx é Bissexto

OBS:Chama-se ano bissexto o ano ao qual é acrescentado um dia extra,
ficando com 366 dias, um dia a mais do que os anos normais de 365 dias, ocorrendo a cada quatro anos
(exceto anos múltiplos de 100 que não são múltiplos de 400).

"""
# Minha solução:
from datetime import datetime
ano_atual = datetime.now()
ano_atual = int(ano_atual.year)

ano = input('Que ano quer analisar? Digite "a" para analisar o ano atual: ')

if ano == 'a':
    ano = ano_atual
else:
    ano = int(ano)

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto')
"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores.
SAÍDA:
Em que ano a 1° pessoa nasceu?
Em que ano a 2° pessoa nasceu?
Em que ano a 3° pessoa nasceu?
Em que ano a 4° pessoa nasceu?
Em que ano a 5° pessoa nasceu?
Em que ano a 6° pessoa nasceu?
Em que ano a 7° pessoa nasceu?

Ao todo tivemos X pessoas maiores de idade
E também tivemos Y pessoas menores de idade
"""
from datetime import date

ano_atual = int(date.today().year)

contador = 1
maior = 0
menor = 0
while contador <= 7:
    n = int(input(f'Em que ano a {contador}° pessoa nasceu? '))
    x = ano_atual - n
    if x >= 18:
        maior += 1
    elif x < 18:
        menor += 1
    contador += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menores de idade')

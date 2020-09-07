"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

SAÍDA:
Primeiro aluno: Paulo
Segundo aluno: Ana
Terceiro aluno: Pedro
Quarto aluno: Maria
O aluno escolhido foi ?????

"""
# Minha solução:
import random
primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')
lista = [primeiro, segundo, terceiro, quarto]
sorteio = random.choice(lista)
print(f'O aluno escolhido foi {sorteio}')
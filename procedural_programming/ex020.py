"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
SAÍDA:
Primeiro aluno:
Segundo aluno:
Terceiro aluno:
Quarto aluno:
A ordem de apresentação será
['???????', '???????', '??????', '????????']

"""
# Minha solução 1:
import random
primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')

lista = [primeiro, segundo, terceiro, quarto]
sorteio = random.sample(lista, 4)
print('A ordem de apresentação será')
print(sorteio)

# Minha solução 2:
random.shuffle(lista)
print('A ordem de apresentação será')
print(lista)
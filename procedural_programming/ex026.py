"""
Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "A".
Em que posição ela aparece a primeira vez.
Em que posição ela parece a última vez.
SAÍDA:
Digite uma frase:    Amanda ama Pedro
A letra A aparece 5 vezes na frase.
A primeira letra A apareceu na posição 1
A última letra A apareceu na posição 10
"""

# Minha solução:
frase = input('Digite uma frase: ').lower().strip()

qntd_a = frase.count('a')
primeiro_a = frase.find('a')+1
ultimo_a = frase.rfind('a')+1

print(f'A letra A aparece {qntd_a} vezes na frase.')
print(f'A primeira letra A apareceu na posição {primeiro_a}')
print(f'A última letra A apareceu na posição {ultimo_a}')

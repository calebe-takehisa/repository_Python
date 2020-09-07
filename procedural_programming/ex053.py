"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
SAÍDA:
Digite uma frase: batata frita
O inverso de batatafrita é atirfatatab
A frase digitada não é um palíndromo!

Temos um palíndromo!
"""

frase = input('Digite uma frase: ').upper().replace(" ", "")
inverso = frase[::-1]
print(f'O inverso de {frase} é {inverso}')
if frase == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

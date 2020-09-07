"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o númeor solicitado for negativo.

SAÍDA:
Quer ver a tabuada de qual valor? 8
------------------------------------
8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
8 x 5 = 40
8 x 6 = 48
8 x 7 = 56
8 x 8 = 64
8 x 9 = 72
8 x 10 = 80
------------------------------------
Quer ver a tabuada de qual valor? -9
------------------------------------
PROGRAMA TABUADA ENCERRADO. Volte sempre!
"""

while True:
    number = int(input('Quer ver a tabuada de qual valor? '))
    print(f'-'*35)
    if number < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    else:
        for x in range(1, 11):
            print(f'{number} x {x} = {number * x}')
        print(f'-' * 35)

"""
Refaça o DESAGIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
SAÍDA:
Digite um número para ver sua tabuada: X
X x 1 = Y
X x 2 = Y
X x 3 = Y
X x 4 = Y
X x 5 = Y
X x 6 = Y
X x 7 = Y
X x 8 = Y
X x 9 = Y
X x 10 = Y

"""
n = int(input('Digite um número para ver sua tabuada: '))
for x in range(1, 11):
    print(f'{n} x {(x):2} = {n * x}')

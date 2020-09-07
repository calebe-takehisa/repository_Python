"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.
SAÍDA:
10
9
8
7
6
5
4
3
2
1
0
BUM! BUM! POOOW!
"""
import time

for x in range(10, -1, -1):
    time.sleep(1)
    print(x)
    if x == 0:
        print('BUM! BUM! POOOW!')


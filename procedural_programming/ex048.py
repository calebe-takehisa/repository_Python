"""
Faça um programa que calcule a soma entre todos os números ímpares
que são múltiplos de três e que se encontram no intervalo de 1 até 500.
SAÍDA:
A soma de todos os 83 valores solicitados é 20667

"""
valores = 0
soma = 0
for n in range(1, 501):
    if n % 2 == 1:
        if n % 3 == 0:
            valores += 1
            soma += n

print(f'A soma de todos os {valores} valores solicitados é {soma}')
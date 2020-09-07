"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.

SAÍDA:
Informe seu sexo [M/F]: n
Dados inválidos. Por favor, informe seu sexo: l
Dados inválidos. Por favor, informe seu sexo: w
Dados inválidos. Por favor, informe seu sexo: m
Sexo M registrado com sucesso

"""
sexo = input('Informe seu sexo [M/F]: ').strip().upper()

while sexo not in 'MF':
    sexo = input('Dados inválidos. Por favor, informe seu sexo [M/F]: ').strip().upper()

print(f'Sexo {sexo} registrado com sucesso')

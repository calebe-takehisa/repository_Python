"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
SAÍDA:
Qual é o salário do funcionário? R$xxxx.xx
Quem ganhava R$xxxx.xx passa a ganhar R$xyyy.xx agora.

"""
# Minha solução:
salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    novo_salario = salario * 1.15
else:
    novo_salario = salario * 1.10

print(f'Quem ganhava R${salario:.2f} passa a ganhar R${novo_salario:.2f} agora.')
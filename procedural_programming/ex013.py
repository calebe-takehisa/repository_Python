"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
SAÍDA:
Qual é o salário do Funcionário? R$4319.43
Um funcionário que ganhava R$4319.43, com 15% de aumento, passa a receber R$4967.34

"""
# Minha solução:
salario = input('Qual é o salário do Funcionário? R$')
reajuste = 15
novo_salario = (float(salario)*reajuste/100)+float(salario)
print(f'Um funcionário que ganhava R${salario}, com {reajuste}% de aumento, passa a receber R${novo_salario:.2f}')



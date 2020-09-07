"""
Escreva um programa que leia a velocidade de uma carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.

SAÍDA:
Qual é a velocidade atual do carro? x
Acima de 80km:
MULTADO! Você excedeu o limite permitido que é de 80km/h
Você deve pagar uma multa de R$XXX,XX!
Tenha um bom dia! Dirija com segurança!

Abaixo de 80km:
Tenha um bom dia! Dirija com segurança!

"""
# Minha solução:
velocidade = int(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Tenha um bom dia! Dirija com segurança!')
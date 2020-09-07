"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
-Abaixo de 18.5: Abaixo do Peso
-Entre 18.5 e 25: Peso ideal
-25 até 30: Sobrepeso
-30 até 40: Obesidade
-Acima de 40: Obesidade mórbida
Calculo IMC (altura x altura)/peso
SAÍDA:
Qual é seu peso(Kg)? zzz
Qual é sua altura(m)? mm
O IMC dessa pessoa é de xx.x
Você está ......

"""
def imc(altura, peso):
    imc = peso / (altura ** 2)
    print(f'O IMC é de {imc:.2f}')
    if imc < 18.5:
        print('O IMC indica que está abaixo do peso ideal')
    elif imc < 25:
        print('O IMC indica peso ideal ')
    elif imc < 30:
        print('O IMC indica sobrepeso')
    elif imc <= 40:
        print('O IMC indica obesidade')
    else:
        print('O IMC indica obesidade mórbida')


while True:
    try:
        altura = float(input('Digite a altura(m)? '))
        peso = float(input('Digite o peso(Kg)? '))
        imc(altura, peso)
        break
    except:
        print('Favor digitar apenas valores válidos')

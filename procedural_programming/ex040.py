"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
-Média abaixo de 5.0: REPROVADO
-Média entre 5.0 e 6.9: RECUPERAÇÃO
-Média 7.0 ou superior: APROVADO

SAÍDA:
Primeira nota: X
Segunda nota: X
Tirando X.X e X.X, a média do aluno é Y.Y

Aprovado:
O Aluno está APROVADO.
Recuperação:
O Aluno está em RECUPERAÇÃO.
Reprovado:
O Aluno está REPROVADO.

"""
# Minha solução:
def media(n1, n2):
    """
    Calcular a média ponderada de 2 notas.
    :param n1: nota 1 com peso 1
    :param n2: ntoa 2 com peso 2
    :return: retorna a média ponderada
    """
    mda = (n1 + (n2*2))/3
    return mda


while True:
    try:
        n1 = float(input('Primeira nota: '))
        n2 = float(input('Segunda nota: '))
        if n1 >= 0 and n1 <= 10 and n2 >= 0 and n2 <= 10:
            m = media(n1, n2)
            print(f'Tirando {n1} e {n2}, a média do aluno é {m:.1f}')
            if m < 5:
                print('O Aluno está REPROVADO.')
                break
            elif m < 7:
                print('O Aluno está em RECUPERAÇÃO.')
                break
            else:
                print('O Aluno está APROVADO.')
                break
        else:
            print('Digite apenas notas válidas de 0 a 10.\n')
    except:
        print('Digite apenas notas válidas de 0 a 10.\n')
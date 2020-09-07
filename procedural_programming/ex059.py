"""
Crie um programa que leia dois valores e mostre um menu como o ao abaixo na tela:
Seu programa deverá realizar a operação solicitada em cada caso.
SAÍDA:
Primeiro valor: X
Segundo valor: Y
	[1] somar
	[2] multiplicar
	[3] maior
	[4] novos números
	[5] sair do programa
Qual é a sua opção? 1
[1]
A soma entre X + Y é Z
=-==-==-==-==-==-==-==-==-==-==-=
[2]
O resultado de X x Y é Z
=-==-==-==-==-==-==-==-==-==-==-=
[3]
Entre X e Y o maior é X
=-==-==-==-==-==-==-==-==-==-==-=
[4]
Informe os números novamente:
Primeiro valor: X
Segundo valor: Y
=-==-==-==-==-==-==-==-==-==-==-=
[5]
Finalizando...
=-==-==-==-==-==-==-==-==-==-==-=
Fim do programa! Volte sempre!

OBS: número erro mensagem:
Opção inválida. Tente novamente.
"""


def convnum(n):
    try:
        n = int(n)
        return n
    except:
        try:
            n = float(n)
            return n
        except:
            return


opcao = 0
while opcao != '5':
    n1 = convnum(input('Primeiro valor: '))
    n2 = convnum(input('Segundo valor: '))
    while (type(n1) == int or type(n1) == float) and (type(n2) == int or type(n2) == float):
        print('[1] somar\n'
              '[2] multiplicar\n'
              '[3] maior\n'
              '[4] novos números\n'
              '[5] sair do programa')
        opcao = input('>>>>>Qual é a sua opção? ')
        if opcao == '1':
            print(f'A soma entre {n1} + {n2} é {n1 + n2}\n')
            continue
        elif opcao == '2':
            print(f'O resultado de {n1} x {n2} é {n1 * n2}\n')
            continue
        elif opcao == '3':
            if n1 > n2:
                print(f'Entre {n1} e {n2} o maior é {n1}\n')
            elif n1 < n2:
                print(f'Entre {n1} e {n2} o maior é {n2}\n')
            else:
                print(f'Os números {n1} e {n2} são iguais\n')
        elif opcao == '4':
            print('\nInforme os números novamente:')
            break
        elif opcao == '5':
            print('Finalizando...')
            print('=-' * 20)
            break
        else:
            print('Opção inválida. Tente novamente.')
            continue
    else:
        print('Digite apenas números')

print('Fim do programa! Volte sempre!')

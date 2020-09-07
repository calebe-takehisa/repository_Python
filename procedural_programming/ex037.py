"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal
SAÍDA:
Digite um número inteiro: xxx
Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
Sua opção: y
xxx convertido para HEXADECIMAL é igual a xx

"""
# Minha solução:
while True:
    num = input('Digite um número inteiro:')
    print('Escolha uma das bases para conversão:'
                 '\n[ 1 ] converter para BINÁRIO'
                 '\n[ 2 ] converter para OCTAL'
                 '\n[ 3 ] converter para HEXADECIMAL')
    opcao = input('Sua opção: ')
    try:
        if opcao == '1':
            b = bin(int(num))[2::1]#binario
            print(f'{num} convertido para BINÁRIO é igual a {b}\n')
        elif opcao == '2':
            o = oct(int(num))[2::1]#octal
            print(f'{num} convertido para OCTAL é igual a {o}\n')
        elif opcao == '3':
            h = hex(int(num))[2::1]#hexadecimal
            print(f'{num} convertido para HEXADECIMAL é igual a {h}\n')
        else:
            print('Digite opções válidas.\n')
    except:
        print('Digite apenas números inteiros\n')
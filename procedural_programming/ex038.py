"""
Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem.
SAÍDA:
Primeiro número:
Segundo número:
O PRIMEIRO valor é maior
O SEGUNDO valor é maior
Os valores são IGUAIS

"""
# Minha solução:
print('Bem-vindo ao comparador de números')
while True:
    try:
        primeiro = int(input('Primeiro número: '))
        segundo = int(input('Segundo número: '))
        if primeiro == segundo:
            print('Os valores são IGUAIS\n')
        elif primeiro > segundo:
            print('O PRIMEIRO valor é maior\n')
        else:
            print('O SEGUNDO valor é maior\n')
    except:
        print('Digite apenas números inteiros\n')
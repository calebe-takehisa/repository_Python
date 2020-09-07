"""
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

SAÍDA:
Digite um valor: 9.123
O valor digitado foi 9.123 e a sua porção inteira é 9

"""
# Minha solução 1:
valor = float(input('Digite um valor: '))
novo_valor = int(valor // 1)
print(f'O valor digitado foi {valor} e a sua porção inteira é {novo_valor}.')

# Minha solução 2:
valor2 = input('Digite um valor: ')
novo_valor2 = valor2[:1:]
print(f'O valor digitado foi {valor2} e a sua porção inteira é {novo_valor2}.')

# Minha solução 3:
valor3 = input('Digite um valor: ')
print(f'O valor digitado foi {valor3} e a sua porção inteira é {float(valor3):.0f}.')

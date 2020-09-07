"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de
Fibonacci.
Ex:
0 → 1 → 1 → 2 → 3 → 5 → 8

SAÍDA:
_________________________
Sequência de Fibonacci
_________________________
Quantos termos você quer mostrar? 10
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
0 → 1 → 1 → 2 → 3 → 5 → 8 → 13 → 21 → 34 → FIM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

sequence = int(input('Quantos termos você quer mostrar? '))
count = 0
fibonacci_total = 0
fibonacci_term_a = 0
fibonacci_term_b = 1
while count < sequence:
    print(fibonacci_total, end=' → ')
    fibonacci_total = fibonacci_term_a + fibonacci_term_b
    fibonacci_term_b = fibonacci_term_a
    fibonacci_term_a = fibonacci_total
    count += 1

print('FIM')

"""
Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
-Equilátero: Todos os lados são iguais.
-Isósceles: Dois lados são iguais.
-Escaleno: Todos os lados diferentes.

SAÍDA:
Primeiro segmento:
Segundo segmento:
Terceiro segmento:
PODEM FORMAR
Os segmentos acima PODEM FORMAR um Triângulo:
isósceles equilátero ou escaleno
NÃO PODEM FORMAR
Os segmentos acima NÃO PODEM FORMAR Triângulo.

"""
def triangulo(a, b, c):
    l1 = (b - c) < a < (b + c)
    l2 = (a - c) < b < (a + c)
    l3 = (a - b) < c < (a + b)
    print(l1, l2, l3)
    if l1 == True and l2 == True and l3 == True:
        if a == b and a == c:
            return print(f'Os segmentos acima PODEM FORMAR um Triângulo: Equilátero')
        elif a == b or a == c or b == c:
            return print(f'Os segmentos acima PODEM FORMAR um Triângulo: Isósceles')
        elif a != b and a != c and b != c:
            return print(f'Os segmentos acima PODEM FORMAR um Triângulo: Escaleno')
    else:
        return print(f'Os segmentos acima NÃO PODEM FORMAR um triângulo!')


print('-='*16)
print('    Analisador de Triângulos')
print('-='*16)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

triangulo(a, b, c)

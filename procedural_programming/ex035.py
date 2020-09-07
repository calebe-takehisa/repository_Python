"""
Desenvolva um programa que leia o comprimento
de três retas e diga ao usuário se elas podem ou não formar um triângulo.
SAÍDA:
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
     Analisador de Triângulos
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Primeiro segmento:
Segundo segmento:
Terceiro segmento:
Os segmentos acima PODEM FORMAR um triângulo!
Os segmentos acima NÃO PODEM FORMAR um triângulo!

"""
# Minha solução:
print('-='*16)
print('    Analisador de Triângulos')
print('-='*16)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

l1 = (b - c) < a < (b + c)
l2 = (a - c) < b < (a + c)
l3 = (a - b) < c < (a + b)

if l1 == True and l2 == True and l3 == True:
    print(f'Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print(f'Os segmentos acima NÃO PODEM FORMAR um triângulo!')
"""
Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.
SAÍDA:
Gerador de PA
-=-=-=-=-=-=-=-=-=
Primeiro termo: 2
Razão da PA: 5
2 → 7 → 12 → 17 → 22 → 27 → 32 → 37 → 42 → 47 → FIM

"""
print('='*40)
print('10 Termos de uma  Progressão Aritmética')
print('='*40)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

contador = 0
while contador < 10:
    print(f'{primeiro_termo}', end=' → ')
    primeiro_termo += razao
    contador += 1

print('ACABOU')
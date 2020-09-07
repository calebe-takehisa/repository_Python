"""
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
SAÍDA:
Gerador de PA
-=-=-=-=-=-=-=-=-=
Primeiro termo: 2
Razão da PA: 5
2 → 7 → 12 → 17 → 22 → 27 → 32 → 37 → 42 → 47 → PAUSA
Quantos termos você quer mostrar a mais? 2
52 → 57 → PAUSA
Quantos termos você quer mostrar a mais? 0
Progressão finalizada com 12 termos mostrados.

"""
import pacotes.formata

print('-=' * 10)
print('Gerador de PA')
print('-=' * 10)
termo = pacotes.formata.numif(input('Primeiro termo: '))
razao = pacotes.formata.numif(input('Razão da PA: '))

total_termos = termo
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{total_termos}', end=' → ')
        total_termos += razao
        contador += 1
        if contador == total+1:
            print('PAUSA')
    mais = pacotes.formata.numif(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {contador-1} termos mostrados.')
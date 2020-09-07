"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo.

SAÍDA:
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
VAMOS JOGAR PAR OU ÍMPAR
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Diga um valor: 8
Par ou Ímpar? [P/I] P
-----------------------------
Você jogou 8 e o computador 4. Total de 12 DEU PAR
-----------------------------
Você VENCEU!
Vamos jogar novamente...
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Diga um valor: 4
Par ou Ímpar? [P/I] P
Você jogou 4 e o computador 3. Total de 7 DEU ÍMPAR
-----------------------------
Você PERDEU!
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
GAME OVER! Você venceu 1 vezes.
"""
from random import randint


def even_odd(number):
    if number % 2 == 0:
        return 'p'
    else:
        return 'i'


def victory_message():
    print('-' * 28)
    print('Você VENCEU!')
    print('Vamos jogar novamente...')
    print('-=' * 14)


def lose_message():
    print('-' * 28)
    print('Você PERDEU!')
    print('-=' * 14)


print('-=' * 14)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 14)

win = True
number_wins = 0
while win:
    player_number = int(input('Diga um valor: '))
    even_or_odd = input('Par ou Ímpar? [P/I] ').lower()
    computer_number = randint(1, 10)
    total_number = player_number + computer_number
    print('-' * 28)

    if even_odd(total_number) == 'p':
        print(f'Você jogou {player_number} e o computador {computer_number}. Total de {total_number} DEU PAR')
        if even_or_odd == 'p':
            victory_message()
            number_wins += 1
        else:
            win = False
            lose_message()

    elif even_odd(total_number) == 'i':
        print(f'Você jogou {player_number} e o computador {computer_number}. Total de {total_number} DEU ÍMPAR')
        if even_or_odd == 'i':
            victory_message()
            number_wins += 1
        else:
            win = False
            lose_message()

print(f'GAME OVER! Você venceu {number_wins} vezes.')

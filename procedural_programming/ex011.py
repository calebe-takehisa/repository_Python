"""
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2m².

SAÍDA:
Largura da parede:
Altura da parede:
Sua parede tem a dimensão de ll.llxaa.aa e sua área é de m.mm m².
Para pintar essa parede, você precisará de t.tt litros de tinta.
"""
# Minha solução:
largura = input('Largura da parede: ')
altura = input('Altura da parede: ')
area = float(largura) * float(altura)
tinta = float(area)/2
print(f'Sua parede tem a dimensão de {float(largura):.1f}x{float(altura):.1f} e sua área é de {float(area):.1f}m².')
print(f'Para pintar essa parede, você precisará de {float(tinta):.1f}l de tinta.')
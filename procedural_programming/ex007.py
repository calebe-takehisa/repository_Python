"""
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

SAÍDA:
Primeira nota do aluno: x
Segunda nota do aluno: y
A média entre x e y é igual a z.z

"""
# Minha solução:
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
print(f'A média entre {(n1):.1f} e {(n2):.1f} é igual a {((n1 + n2) / 2):.1f}')

# Solução do Professor:
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
média = (n1 + n2) / 2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, média))
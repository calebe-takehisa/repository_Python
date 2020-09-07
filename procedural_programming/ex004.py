"""
Crie um dissecador de variável, conforme exemplo abaixo:

SAÍDA:
Digite algo: Calebe
O tipo primitivo desse valor é: <class 'str'>
Só tem espaços? False
É um número? False
É alfabético? True
É alfanumérico? True
Está em maiúsculas? False
Está em minúsculas? False
Está capitalizada? True


"""
# Minha solução:
variavel = input('Digite algo: ')
print(f'O tipo primitivo desse valore é: {type(variavel)}')#
print(f'Só tem espaços? {variavel.isspace()}')#
print(f'É um número? {variavel.isdigit()}')
print(f'É alfabético? {variavel.isalpha()}')
print(f'É alfanumérico? {variavel.isalnum()}')
print(f'Está todo em maiúsculo? {variavel.isupper()}')
print(f'Está todo em minúsculo? {variavel.islower()}')
print(f'Está com a primeira letra em maiúsculo? {variavel.istitle()}')

# Solução do Professor:
a = input('Digite algo: ')
print('O tipo primitivo desse valor é:', type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Está em maiúsculas?', a.isupper())
print('Está em minúsculas?', a.islower())
print('Está capitalizada?', a.istitle())
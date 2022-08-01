#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

n1 = float(input('Insira a medida do primeiro lado: '))
n2 = float(input('Insira a medida do segundo lado: '))
n3 = float(input('Insira a medida do terceiro lado: '))

if n1 + n2 > n3 and n2 + n3 > n1 and n1 + n3 > n2:
    print('Pode ser formado um triangulo!')
else:
    print('Não pode ser formado um triangulo!')

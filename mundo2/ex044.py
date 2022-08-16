'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
'''

#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

n1 = float(input('Insira a medida do primeiro lado: '))
n2 = float(input('Insira a medida do segundo lado: '))
n3 = float(input('Insira a medida do terceiro lado: '))

if n1 + n2 > n3 and n2 + n3 > n1 and n1 + n3 > n2:
    print('Pode ser formado um triangulo!')
    if n1 == n2 == n3:
        print('É um triangulo equilatero!')
    elif n1 != n2 != n3 != n1:
        print('É um triangulo escaleno!')
    else:
        print('É um triangulo isósceles!')
else:
    print('Não pode ser formado um triangulo!')

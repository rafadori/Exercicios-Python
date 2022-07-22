#faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possiveis sobre ele

'''
n1 = str(print('Isto é alfanumérico, 1, 2 e 3'))
print(type(n1))
print(n1.isalnum())

n2 = input('Digite algo: ')
print(n2.isnumeric())
'''

valor = (input('Digite algo: '))
tipo = (type(valor))
print('O tipo primitivo desse valor é: {} '.format(tipo))
espaco = (valor.isspace())
print('Só tem espaços? {} '.format(espaco))
numero = (valor.isnumeric())
print('É um numero? {} '.format(numero))
alpha = (valor.isalpha())
print('É alfabetico? {} '.format(alpha))
alnum = (valor.isalnum())
print('É alfanumérico? {} '.format(alnum))
upper = (valor.isupper())
print('Está em maiusculas? {} '.format(upper))
lower = (valor.islower())
print('Está em minusculas? {} '.format(lower))
title = (valor.istitle())
print('Está capitalizada? {} '.format(title))

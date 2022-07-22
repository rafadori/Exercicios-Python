#faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possiveis sobre ele

n1 = str(print('Isto é alfanumérico, 1, 2 e 3'))
print(type(n1))
print(n1.isalnum())

n2 = input('Digite algo: ')
print(n2.isnumeric())
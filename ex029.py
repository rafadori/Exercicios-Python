#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: '))
split_nome = nome.split()
print('Seu primeiro nome é {}'.format(split_nome[0]))
print('Seu ultimo nome é {}'.format(split_nome[-1]))

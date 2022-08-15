#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

valor = int(input('Digite um numero inteiro: '))
print('Escolha qual base de conversão: ')
print('[ 1 ] para binario')
print('[ 2 ] para octal')
print('[ 3 ] para hexadecimal\n...')
resposta = int(input())

binario = format(valor, "b")
octa = format(valor, "o")
hexa = format(valor, "x")

if resposta == 1:
    print('O número em binário é igual a:\n',binario)
elif resposta == 2: 
    print('O número em octal é igual a:\n',octa)
elif resposta == 3: 
    print('O número em hexadecimal é igual a:\n',hexa)
else:
    print('Tente novamente!')

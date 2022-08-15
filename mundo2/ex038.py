#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

import os, time

os.system('cls' if os.name == 'nt' else 'clear')

print('Bem vindo ao empréstimo bancário\nVamos dar início a simulação')
time.sleep(2)
print('...')
time.sleep(2)

valor_casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o salário do comprador? R$ '))
anos = int(input('Em quantos anos pretende pagar a casa? '))

meses = anos * 12
prestacao = valor_casa / meses

if prestacao > salario * 0.3:
    print('Empréstimo negado..')
else:
    print('Emprestimo aprovado!')

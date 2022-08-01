#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário: R$ '))
aumento1 = (salario * 0.15) + salario
aumento2 = (salario * 0.10) + salario
if salario <= 1250.00:
    print('O salário subiu para R$ {:.2f}'.format(aumento1))
else:
    print('O salário subiu para R$ {:.2f}'.format(aumento2))

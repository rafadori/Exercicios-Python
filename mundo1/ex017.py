import os

os.system('clear') or None

print('Localiza, locadora de carros\nSeja bem vindo!\nVamos calcular todos seus custos, para isso responda as perguntas abaixo:')
dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram rodados? '))
valor_dias = dias * 60
valor_km = km * 0.15
total = valor_dias + valor_km

print('O custo total da alocação é de R${:.2f}'.format(total))
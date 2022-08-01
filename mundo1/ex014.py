#calculando descontos

preco = float(input('Insira o valor de um produto: '))
desconto = preco - (preco * 0.05) #desconto de 5%
print('O produto custava R${:.2f} e com desconto de 5% aplicado está custando R${:.2f}'.format(preco, desconto))
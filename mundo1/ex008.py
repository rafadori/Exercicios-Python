# dobro, triplo e raiz quadrada de um numero

import os

n1 = int(input('Insira um numéro: '))
dobro = n1 * 2
triplo =  n1 * 3
raiz = n1 ** (1/2) # o sinal de ** é de exponenciação

os.system('cls') or None #caso esteja fora do Windows substitua o 'cls' por 'clear'

print('O valor inserido foi:', n1)
print('O dobro de {} é {}'.format(n1, dobro))
print('O triplo de {} é {}'.format(n1, triplo))
print('A raiz quadrada de {} é {}'.format(n1, raiz)) # da pra formatar também colocando dentro das {} quantas casas decimais vamos querer, como por exemplo {:.2f}
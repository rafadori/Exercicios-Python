#jogo de advinhação

import random

num = random.randint(0, 5)

print('Jogo da advinhação!\nAdvinhe qual o número entre 0 e 5: ')
valor = int(input('Insira o valor: '))
if valor == num:
    print('Você acertou!')
else:
    print('Tente novamente! O número sorteado foi {}'.format(num))

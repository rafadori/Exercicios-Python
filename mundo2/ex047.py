#Jokenpo
from time import sleep
import os, random

os.system('cls' if os.name == 'nt' else 'clear')

print('''Escolha uma opção:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
''')
sleep(1)
jokenpo = int(input('Qual sua jogada? '))
sleep(1)
print('...')
sleep(1)
print('Jokenpo!!')
sleep(1)

computador = random.randint(1,3)

print('Jogador escolheu: {} '.format(jokenpo))
sleep(2)
print('Computador escolheu: {} '.format(computador))
sleep(2)

if jokenpo == 1 and computador == 2:
    print('Computador venceu!')
elif jokenpo == 2 and computador == 1:
    print('Jogador venceu!')
elif jokenpo == 1 and computador == 3:
    print('Jogador venceu!')
elif jokenpo == 3 and computador == 1:
    print('Computador venceu!')
elif jokenpo == 3 and computador == 2:
    print('Jogador venceu!')
elif jokenpo == 2 and computador == 3:
    print('Computador venceu!')
else:
    print('Empate!')

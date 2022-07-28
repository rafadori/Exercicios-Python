#radar de velocidade

import os
import time

os.system('cls') or None

velocidade = int(input('Qual velocidade você está dirigindo? ')) #limite da via 80km
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Tenha um bom dia, dirija com segurança!')
else:
    print('Você será multado por excesso de velocidade!\nCalculando multa...')
    time.sleep(3)
    print('Multa de R${:.2f}, favor regularizar!'.format(multa))

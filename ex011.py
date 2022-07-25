#tabuada
import os
os.system('clear') or None

print('Bem vindo ao gerador de tabuada!\nLembrando que os valores serão multiplicados no máximo por 10')

tabuada = int(input('Para iniciarmos, digite um numéro inteiro: '))

for i in range(0, 10):
    print('{} x {} = {}'.format(tabuada, i + 1, tabuada * (i + 1)))

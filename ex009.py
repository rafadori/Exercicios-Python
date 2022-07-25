#média aritmetica
import os

os.system('clear') or None #use 'cls' se estiver usando windows

n1 = int(input('Digite a primeira nota do aluno: ')) 
n2 = int(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2

print('A média do aluno é {}'.format(media))
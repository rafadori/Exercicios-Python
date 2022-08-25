#faça um programa que leia um int e diga se ele é ou não um numero primo

num = int(input('Insira um número: '))
total = 0
for n in range(1, num + 1):
    if num % n == 0:
        total += 1 #essa repetição irá contar quantas vezes um numero é divisivel
if total == 2:
    print('É número primo!')
else:
    print('Não é um número primo!')

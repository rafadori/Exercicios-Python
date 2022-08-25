#ler o primeiro termo e a razao de uma PA, no final mostrar os 10 primeiros termos dessa progressão
print('Progressão Aritmética')
x = int(input('Primeiro termo: '))
y = int(input('Razão: '))
pa = int(input('Progessão Aritmética: '))
termo = x + (pa - 1) * y
for n in range(x, termo + y, y):
    print(n, end=' => ')
print('Fim')

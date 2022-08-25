# ler seis numeros inteiros e mostrar a soma apenas daqueles que forem par
soma = 0
for n in range (0, 6):
    num = int(input('Digite seis números: '))
    if num % 2 == 0:
        soma += num
print(soma)
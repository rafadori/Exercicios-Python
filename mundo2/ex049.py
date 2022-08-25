#soma entre todos numeros impares multiplos de tres e que se encontram no intervalo de 1 até 500
import os
os.system('cls' if os.name == 'nt' else 'clear')

soma = 0
soma2 = 0
cont = 0 # contador
#exemplo usando list comprehension:
resultado = [num for num in range(0, 500) if num % 2 != 0 and num % 3 == 0]
soma = sum(resultado)
print(soma)

#utilizando loop for:
for num in range(0, 500):
    if num % 2 != 0 and num % 3 == 0:
        cont = cont + 1
        soma2 = soma2 + num
print('A soma de {} valores é igual a: {}'.format(cont, soma2))


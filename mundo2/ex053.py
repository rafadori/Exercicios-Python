#crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando espaços

frase = str(input('Digite sua frase aqui: ')).strip().lower()
print(frase, frase[::-1])

#inverter: [::-1]
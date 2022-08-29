#crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando espaços

frase = str(input('Digite sua frase aqui: ')).strip().lower().replace(' ', '')
if frase == frase[::-1]:
    print('É palindromo')
else:
    print('Não é palindromo')
#print(frase, frase[::-1])

#inverter: [::-1]

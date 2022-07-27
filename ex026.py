#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"

cidade = input('Qual cidade você nasceu? ').strip().lower()
divisao = cidade.split()
if "santo" in divisao[0]:
    print('True')
else:
    print('False')

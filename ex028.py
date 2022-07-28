#primeira e ultima ocorrencia de uma string

letra_a = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(letra_a.count('A')))
print('A letra A aparece pela primeira vez na posição {}'.format(letra_a.find('A')))
print('A letra A aparece pela ultima vez na posição {}'.format(letra_a.rfind('A')))

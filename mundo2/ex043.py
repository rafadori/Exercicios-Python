#niveis de senioridade

from datetime import date

ano_atual = date.today().year
ano_nasc = int(input('Digite qual ano você nasceu: '))
idade = ano_atual - ano_nasc
print('Você tem {} anos'.format(idade))
if idade <= 9:
    print('Você é [MIRIM]!')
elif idade <= 14:
    print('Você é [INFANTIL]!')
elif idade <= 19:
    print('Você é [JUNIOR]!')
elif idade <=25:
    print('Você é [SENIOR]!')
else:
    print('Você é [MASTER]!')
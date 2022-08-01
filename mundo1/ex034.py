#ano bissexto

import calendar

ano = int(input('Insira o ano para verificar se ele é bissexto: '))
if calendar.isleap(ano):
    print('É bissexto!')
else:
    print('Não é bissexto!')

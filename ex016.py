#conversor de temperaturas

celsius = float(input('Insira a temperatura em Celsius a ser transformada: '))
fahr = (celsius * 9/5) + 32
print('{} grau Celsius é igual a {} grau Fahrenheit'.format(celsius, fahr))
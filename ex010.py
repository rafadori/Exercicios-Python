#conversos de medidas

n1 = float(input('Insira a distancia em metros a ser transformada: '))
dec = n1 * 10
cm = n1 * 100
hec = n1 / 100
mm = n1 * 1000
km = n1 / 1000

print('{} metros convertidos para milimetros é igual a: {}'.format(n1, mm))
print('{} metros convertidos para centimetros é igual a: {}'.format(n1, cm))
print('{} metros convertidos para kilometros é igual a: {}'.format(n1, km))
print('{} metros convertidos para decimetros é igual a: {}'.format(n1, dec))
print('{} metros convertidos para hectometros é igual a: {}'.format(n1, hec))
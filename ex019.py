#catetos e hipotenusa
import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('O valor da hipotenusa é de {}'.format(hi))

#podemos fazer também utilizando a biblioteca math
hi_math = math.hypot(co, ca)
print('Utilizando a biblioteca math, o valor da hipotenusa é {}'.format(hi_math))




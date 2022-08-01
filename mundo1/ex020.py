#seno, cosseno e tangente

import math, cmath

angulo = float(input('Digite o angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente =  math.tan(math.radians(angulo))
print('O angulo de {} tem seno de {}, cosseno de {} e tangente de {}'.format(angulo, seno, cosseno, tangente))

#decompondo um número
import math

numero = int(input('Digite um número: '))
print('Analisando número...')
unidade = numero % 10
dezena = (numero - unidade) / 10 % 10
pre_cent = (numero - unidade) / 10
centena = (pre_cent - dezena) / 10
print('A unidade do número é {}, sua dezena é {} e sua centena é {}'.format(unidade, math.trunc(dezena), math.trunc(centena)))

#seguindo outra logica de programação

d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('A unidade do número é {}, sua dezena é {}, a centena é {} e seu milhar é {}'.format(unidade, d, c , m))

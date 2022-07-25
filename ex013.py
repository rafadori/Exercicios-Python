#considere o seguinte: a cada 2m² é gasto 1L de tinta para pintar 
import os

os.system('clear') or None

print('Pintando a parede!')
largura = float(input('Insira a largura da parede: '))
altura = float(input('Insira a altura da parede: '))
area = largura * altura
tinta = area / 2
os.system('clear') or None
print('Sua parede tem dimensão de {} X {} e sua área é de {}m²'.format(largura, altura, area))
print('A quantidade de tinta necessaria para pinta-la é de {} litros'.format(tinta))


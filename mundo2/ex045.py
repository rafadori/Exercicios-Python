#descobrindo IMC

massa = float(input('Qual o seu peso? (Kgs): '))
altura = float(input('Qual sua altura? (Cms): '))
imc = massa / (altura ** 2)
print('Seu IMC é de {:.1f}'.format(imc))
'''
– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
'''
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso')
elif imc >= 30 and imc < 40:
    print('Você está obeso!')
else:
    print('Você está em obesidade mórbida')
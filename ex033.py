#custo de viagem

viagem_km = int(input('Sua viagem será de quantos Kms? ' ))
if viagem_km <= 200:
    print('O valor da viagem é de: R$', viagem_km * 0.50)
else:
    print('O valor da viagem é de: R$', viagem_km * 0.45)

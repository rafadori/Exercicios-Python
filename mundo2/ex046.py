#loja de compra
print('Lojas Python\nFormas de pagamento:\n[ 1 ] à vista dinheiro/pix\n[ 2 ] à vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão')

valor = float(input('Qual o valor total da compra? R$ '))
desconto10 = valor - (valor * 0.1) 
desconto5 = valor - (valor * 0.05)
juros = valor + (valor * 0.2)
forma_pagamento = (int(input('Escolha uma forma de pagamento: ')))

if forma_pagamento == 1:
    print('Pagamento a vista no dinheiro/pix escolhido!\nSua compra no valor de R${:.2f} tem desconto de 10%, ficando num total de {:.2f} reais'.format(valor, desconto10))
elif forma_pagamento == 2:
    print('Pagamento à vista no cartão escolhido!\nSua compra no valor de R${:.2f} tem desconto de 5%, ficando num total de {:.2f} reais'.format(valor, desconto5))
elif forma_pagamento == 3:
    print('Pagamento em 2x no cartão escolhido!\nSua compra irá sair no valor de R$ {:.2f} e não tem desconto'.format(valor))
elif forma_pagamento == 4:
    parcelas = (int(input('Quantas parcelas? ')))
    valor_parcelas = valor / parcelas
    print('Pagamento em 3x ou mais no cartão escolhido!\nSua compra no valor de R$ {:.2f} será feita em {}x de R$ {:.2f} cada com juros de 20% e irá sair no valor total de {:.2f} reais'.format(valor, parcelas, valor_parcelas, juros))
else:
    print('Opção inválida, tente novamente!')

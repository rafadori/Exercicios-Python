#analisador de textos

nome = input('Digite seu nome completo: ').strip()
print('Seu nome em maiúsculas é', nome.upper())
print('Seu nome em minúsculas é', nome.lower())
print('Seu nome tem ao todo', len(nome) - nome.count(' '), 'letras') 
divisao = nome.split()
print('Seu primeiro nome é', divisao[0], 'e tem', len(divisao[0]), 'letras')

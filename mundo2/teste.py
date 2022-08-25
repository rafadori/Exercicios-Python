'''
lista = [50, 100, 200]
#usando loop for
nova_lista = []
for i in lista:
    nova_lista.append(i * 2)

print(lista)
print(nova_lista)

#usando list comprehension

lista2 = [preco * 2 for preco in lista]

print(lista)
print(lista2)

'''

lista = [50, 100, 200]
imposto = []

for preco in lista:
    if preco > 99:
        imposto.append((preco * 0.5) + preco)
print(imposto)

#fazendo com list comprehension

imposto2 = [(preco * 0.5) + preco for preco in lista if preco > 99]
print(imposto2)
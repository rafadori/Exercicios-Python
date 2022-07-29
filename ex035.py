#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))

#para facilitar a lógica envolvida declaramos o maior número e montamos o restante em cima disso
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print('O maior número é: {} '.format(maior))

menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print('O maior número é: {} '.format(menor))

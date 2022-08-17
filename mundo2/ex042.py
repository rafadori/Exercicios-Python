#calculando media

n1 = float(input('Insira a primeira nota do aluno: '))
n2 = float(input('Insira a segunda nota do aluno: '))
media = (n1 + n2) / 2
print('A nota do bimestre desse aluno foi {}'.format(media))
if media <= 5:
    print('Aluno reprovado!')
elif media > 5 and media < 7.5:
    print('Você está de recuperação!')
else:
    print('Você está aprovado!')

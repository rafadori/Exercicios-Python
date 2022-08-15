#ano de alistamento

from datetime import date

nascimento = int(input('Digite o ano que você nasceu: '))
ano_atual = date.today().year
idade_atual = ano_atual - nascimento
idade_alistamento = 18

print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade_atual, ano_atual))

if idade_atual == idade_alistamento:
    print('Está na hora de servir!')
elif idade_atual > idade_alistamento:
    print('Você devia ter se alistado {} ano(s) atrás'.format(idade_atual - idade_alistamento))
    print('Seu alistamento foi em {}'.format(ano_atual - (idade_atual - idade_alistamento)))
elif idade_atual < idade_alistamento:
    print('Ainda faltam {} ano(s) para você servir'.format(idade_alistamento - idade_atual))
    print('Seu alistamento vai ser em {}'.format(ano_atual + (idade_alistamento - idade_atual)))

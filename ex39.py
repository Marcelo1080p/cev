from datetime import date
atual = date.today().year
data = int(input('Digite o ano de seu nascimento: '))
idade = atual - data
print('Quem nasceu em {} tem {} anos em {}.'.format(data, idade, atual))
if idade == 18:
    print('Você tem q se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18anos. faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será é {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria  ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {} ano'.format(ano))

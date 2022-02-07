from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento do Atleta: '))
idade = atual - ano
if idade <= 9:
    print('O Atleta tem {} Anos! Categoria: Mirim.'.format(idade))
elif idade <= 14:
    print('O Atleta tem {} Anos! Categoria: Infantil.'.format(idade))
elif idade <= 19:
    print('O Atleta tem {} Anos! Categoria: Junior.'.format(idade))
elif idade <= 25:
    print('O Atleta tem {} Anos! Categoria: Sênior.'.format(idade))
elif idade >= 26:
    print('O Atleta tem {} Anos! Categoria: Master.'.format(idade))
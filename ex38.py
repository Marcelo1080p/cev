print('DESCUBRA QUAL VALOR É MAIOR ABAIXO!')
first = int(input('Digite um Valor: '))
two = int(input('Digite outro valor: '))
if first > two:
    print('{} é maior que {}'.format(first, two))
elif first < two:
    print('{} é maior que {}'.format(two, first))
elif first == two:
    print('{} e {} São o mesmo Número'.format(first, two))

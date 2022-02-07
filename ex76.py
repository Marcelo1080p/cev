
produtos = (('Lápis', 1.75,
             'Borracha', 2,
             'Caderno', 24,
             'Livro', 19.90,
             'Lapizeira', 2.75,
             'Mochila', 69.99))
print('='*38)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('='*38)
for item in range(len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<30}', end='')
    else:
        print(f'R${produtos[item]:>5.2f}')
print("="*39)

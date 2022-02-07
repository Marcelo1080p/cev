while True:
    n = int(input('Deseja ver qual Tabuada? '))
    if n < 0:
        break
    print('-+'*15)
    for c in range(1, 11):
        print(f'{n} X {c} = {n * c}')

    print('-+' * 15)
print('Programa de Tabuada Encerrado. Volte Sempre!')
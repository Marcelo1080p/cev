def fatorial(n, show=False):
    '''
    -> Calcula o Fatorial de um número
    :param n:
    :param show:
    :return: O valor do Fatorial de um número n.
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#Programa Principal
print(fatorial(5, show=True))
help(fatorial)

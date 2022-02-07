def func(a, b):
    s = a * b
    print(f'A área de um terrreno é de {a}x{b} é de {s}m²')


print('Controle de Terrenos')
print('\033[33m=\033[m'*21)
a = float(input('Largura (m): '))
b = float(input('Comprimento (m): '))

func(a, b)
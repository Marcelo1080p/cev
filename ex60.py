'''from math import factorial
n = int(input('Digite um número para calcular se Fatorial:'))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''
n = int(input('Digite um número para calcular se Fatorial:'))
c = n
while c > 0:
    print('{} x '.format(c),end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
#print('O fatorial de {} é {}'.format(n, f))
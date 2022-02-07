print('+-'*10)
print('10 TERMOS DE UMA PA')
print('+-'*10)
p = int(input('PRIMEIRO TERMO: '))
r = int(input('RAZÃO: '))
décimo = p + (10 - 1) * r
for c in range(p, décimo + r, r):
    print(c, end='-> ')
print('fim')
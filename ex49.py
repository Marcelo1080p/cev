num = int(input('Digite um número para ver a sua tabuada: '))
print('-+-' * 4)
for c in range(1, 11):

    print('{} x {} = {}'.format(num, c, num * c))
print('-+-' * 4)

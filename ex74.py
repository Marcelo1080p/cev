from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
print('Eu sorteei os valores : ', end=' ')
for n in numeros:
     print(f'{n}', end=' ')
print(f'\nO mairo valor sorteado foi {max(numeros)}')
print(f'O manor valor sorteado foi {min(numeros)}')

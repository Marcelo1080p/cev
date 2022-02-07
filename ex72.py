cont = ('Zero', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO',
        'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ')
while True:
    num = int(input('Digite um número entre 0 e 10: '))
    if 0 <= num <= 10:
        break
    print('TENTE NOVAMENTE.', end='')
print(f'Você digitou {cont[num]}')
list = []
par = []
impar = []
while True:
    list.append(int(input('Digite um número: ')))
    stop = str(input('Quer continuar? [S/N] ')).upper().strip()
    if stop == 'N':
        print('Você finalizou o programa!')
        break
for i, v in enumerate(list):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('=' * 45)
print(f'A lista completa é {list}')
print(f'Os números que são Pares é: {par}')
print(f'Os números Ímpares são: {impar}')

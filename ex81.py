list = []
cont = 0
while True:
    list.append(int(input('Digite um valor: ')))
    cont += 1
    stop = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if stop == 'N':
        break
print(f'Você digitou {cont} elementos.')
list.sort(reverse=True)
print(f'Os valores em ordem decrescente são {list}')
if 5 in list:
    print('Valor 5 encontrado na lista!')
else:
    print('Valor 5 não encontrado na lista!')
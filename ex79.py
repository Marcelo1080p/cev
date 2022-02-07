valores = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor Duplicado! não vou adicionar...')
    cont = str(input('Quer continuar? [S/N]')).strip().upper()
    if cont == 'N':
        break
print('=' * 50)
print(f'Você digitou os valores {sorted(valores)}')
print('=' * 50)

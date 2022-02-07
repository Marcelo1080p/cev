from time import sleep
 
def maior(*num):
    cont = maior = 0
    print('\033[35m~\033[m' * 40)
    print('ANALISANDO OS VALORES PASSADOS..')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.2)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Os valores informados {cont} valores ao todo.')
    print(f'O maior Valor foi {maior}')


#PROGRAMA PRINCIPAL
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1,2)
maior(6)
maior(0)
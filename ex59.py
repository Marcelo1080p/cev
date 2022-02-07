from time import  sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior 
    [ 4 ] novos números 
    [ 5 ] sair do programa''')
    opção = int(input('>>>>>qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma ente {} e {} é igual a {}!'.format(n1, n2, soma))
    elif opção == 2:
        multiplicar = n1 * n2
        print('A multiplicação entre {} e {} é igual a {}!'.format(n1, n2, multiplicar))
    elif opção == 3:
        if n1 > n2:
            print('o {} é maior que {}!'.format(n1, n2))
        else:
            print('O {} é maior que {}!'.format(n2, n1))
    elif opção == 4:
        print('Informe os números desejados!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    else:
        print('OPÇÃO INVÁLIDA!')
    print('=-='*10)
    sleep(2)
print('FIM DO PROGRAMA')
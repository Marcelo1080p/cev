nome = str(input('Digite o Seu nome: ')).strip().upper()
print('Seja muito Bem-vindo {}'.format(nome))
opção = 0
while opção != 5:
    print('''
    [ 1 ] Taboada
    [ 2 ] 
    [ 3 ] 
    [ 4 ]
    [ 5 ] Fechar o programa!''')
    opção = int(input('Informe o numero da opção desejada: '))
    print('+-'*20)
    if opção == 1:
        num = int(input('Digite o número para ver a taboada: '))
        for c in range(1, 11):
            print('{} X {} = {}'.format( num, c, num * c))
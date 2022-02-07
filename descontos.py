nome = str(input('Insira o nome do cliente: ')).strip().upper()
print('Seja muito bem-vindo {}'.format(nome))
print('=-'*11)
print('PROGRAMA DE DESCONTOS')
print('Pagamentos em DÉBITO/DINHEIRO tem descontos de 3%')
print('Pagamentos em Cartão de crédito AVISTA não tem juros, e Parcelas ate 2x não tem juros')
print('Pagamentos com o Cartão da Loja tem 7% de descontos')
print('Pagamentos Parcelados no Cartão de crédito Aparti de 3x é cobrado juros de 3% nas parcelas!')
print('=-'*11)
opção = 0
while opção != 5:
    print('Insira a forma de pagamento do cliente {}'.format(nome))
    print('''
    [ 1 ]  DÉBITO/DINHEIRO 
    [ 2 ]  CRÉDITO AVISTA
    [ 3 ]  CARTÃO DA LOJA
    [ 4 ]  CRÉDITO PARCELADO
    [ 5 ]  FECHAR PROGRAMA''')
    opção = int(input('Informe o número da opção desejada: '))
    if opção == 1:
        valordacompra = float(input('Insira o valor da compra do Cliente(a) {}: R$'.format(nome)))
        desconto = 3
        resultado = valordacompra - (valordacompra*3/100)
        print('O total da compra do cliente {}, foi {}R$ com o desconto de {}%. Ficará por apenas {}R$'.format(nome, valordacompra, desconto, resultado))
    elif opção == 2:
        valordacompra = float(input('Insira o valor da compra do Cliente(a) {}: R$'.format(nome)))
        print('valor da compra do cliente é {}R$ Sem juros!!!'.format(valordacompra))
    elif opção == 3:
        valordacompra = float(input('Insira o valor da compra do Cliente(a) {}: R$'.format(nome)))
        desconto = 7
        resultado = valordacompra - (valordacompra*7/100)
        print('o valor da compra do cliente {}, ficou {} com o desconto do cartão da loja o valor final será {}'.format(nome, valordacompra, resultado))
    elif opção == 4:
        valordacompra = float(input('Insira o valor da compra do Cliente {}: R$'.format(nome)))
        parcela = int(input('Quantas vezes o Cliente(a) {}, deseja Parcela a compra? '.format(nome)))
        if parcela >= 3:
            vezes = (valordacompra / parcela)
            resultado = vezes + (vezes*3/100)
            print('O valor da compra do Cliente {}, deu {}R$, com o parcelamento de {}vezes, o valor das parcelas será {:.2f}R$'.format(nome, valordacompra, parcela, resultado))
print('{:=^40}'.format(' Sejuu Lojas '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTOS 
[ 1 ] Á vista no dinheiro/cheque
[ 2 ] Á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção ? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparcela = int(input('Quantas Parcelas? '))
    parcela = total / totalparcela
    print('Sua compra sera parcelada em {}x de R${:.2f} COM JUROS'.format(totalparcela, parcela))
else:
    total = 0
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
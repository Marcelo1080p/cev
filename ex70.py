total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: ')).strip().upper()
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
         menor = preço
         barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mas de 1000R$')
print(f'O produto mais barato foi {barato} custa R${menor:.2f}')

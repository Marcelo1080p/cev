produto = float(input('Qual é o preço do produto? R$'))
desconto = int(input('Insira o valor do desconto: %'))
valor = produto*desconto/100
resultado = produto-valor
print('O produto que custava R${}, na promoção com o desconto de {}% vai custar {:.2f}'.format(produto, desconto, resultado))
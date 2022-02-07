casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual é o seu Salário? R$'))
anos = int(input('Quantos anos de Financiamento? '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos '.format(casa, anos), end='')
print('a Prestação sera de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Empréstimo RECUSADO!')
salario = float(input('Qual é o valor do funcionário? R$'))
aumento = int(input('Qual o valor percentual do aumento? %'))
total = salario + (salario * aumento / 100)
print('O Funcionário ganhava R${}, com o Aumento de %{}, passa a receber R${:.2f}'.format(salario, aumento, total))
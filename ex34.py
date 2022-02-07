salario = float(input('Qual é o seu salário? '))
if salario <= 1250:
 aumento = (salario * 15 / 100) + salario
else:
    aumento = (salario * 10 / 100) + salario
print('O seu Salário era {:.2f} com o aumento passa a ser {:.2f}'.format(salario, aumento))
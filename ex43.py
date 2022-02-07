peso = float(input('Qual é o seu Peso? Kg'))
altura = float(input('Qual é a sua Altura? m'))
imc = peso / (altura ** 2)
print('O seu Indice de massa muscular é {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você esta abaixo do Peso!')
elif imc <= 24.9:
    print('Peso ideal. Parabéns!')
elif imc <= 29.9:
    print('Levemente acima do Peso!')
elif imc <= 34.9:
    print('Obesidade grau 1')
elif imc <= 39.9:
    print('Obesidade grau 2 (Severa)')
elif imc >= 40:
    print('Obesidade grau 3 (mórbida)')
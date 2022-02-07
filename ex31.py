km = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(km))
if km <= 200:
    print('Valor da viagem é {}R$'.format(km*0.50))
else:
    print('Valor da viagem é {}R$'.format(km*0.45))
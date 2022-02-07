from time import sleep
velocidade = float(input('Qual a velocidade atual do seu Veiculo? '))
multa = (velocidade - 80) * 7
print('Carregando...')
sleep(1)
if velocidade <=80:
    print('Tenha um Bom dia!')
else:
    print('Você deve pagar uma multa de {:.2f}R$ por exeder o limite permitido de 80km/h'.format(multa))
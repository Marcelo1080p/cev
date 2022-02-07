'''nome = str(input('Digite o seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {} '.format(nome.split()[0]))
print('Seu último nome é {}'.format(nome.split()[-1]))'''

tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <=3:
    print('Carro Novo')
else:
    print('Carro Velho')
print('---FIM---')
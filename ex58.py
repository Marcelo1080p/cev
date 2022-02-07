from random import randint
computador = randint(0, 10) #COMPUTADOR!
print('_+_'*14)
print('Acabei de pensar em um número entre 0 e 10.')
print('_+_'*14)
print('Tente ADIVINHAR!')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador <= computador:
            print('Mais... Tente novamente!')
        else:
            print('Menos, tente novamente!')
print('Acertou com {} palpites. Parabéns'.format(palpites))
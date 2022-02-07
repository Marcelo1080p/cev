from random import  randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''JoKenPô
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual opção vai Escolher? '))
print('Jo')
sleep(.5)
print('Ken')
sleep(.5)
print('Pô')
sleep(.5)
if computador == 0: #COMPUTADOR PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHOU!')
    elif jogador == 2:
        print('COMPUTADOR GANHOU!')
    else:
        print('JOGADA INVÁLIDA! ')
elif computador == 1:   #COMPUTADOR PAPEL
    if jogador == 0:
        print('COMPUTADOR GANHOU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:       #COMPUTADOR TESOURA
    if jogador == 0:
        print('JOGADOR GANHOU!')
    elif jogador == 1:
        print('COMPUTADOR GANHOU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA')
print('-+-'*10)
print('O Computador escolheu {}'.format(itens[computador]))
print('O Jogador escolheu {}'.format(itens[jogador]))
print('-+-'*10)

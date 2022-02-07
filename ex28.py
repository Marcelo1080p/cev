from random import randint
from time import sleep
computador = randint(0, 5) #computador
print('='*52)
print('Vou pensar em um número entre 0 e 5. Tente advinhar')
print('='*52)
jogador = int(input('Em que número eu pensei? ')) #jogador
print('Processando...')
sleep(0.5)
if jogador == computador:
    print('Parabens você ganhou!')
else:
    print('Ganhei Eu pensei no {} e não no {}!'.format(computador, jogador))
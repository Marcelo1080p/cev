from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
        print(f'{k} tirou {v} no dado.')
        sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('\033[31m=\033[m'*30)
print('\033[36m  == RANKING DOS JOGADORES ==\033[m')
for i, v in enumerate(ranking):
        print(f'{i+1}ª lugar: {v[0]} com {v[1]}.')
        sleep(0.5)

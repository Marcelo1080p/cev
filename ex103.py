def ficha(nome='Desconhecido', gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato')


#PROGRAMA PRINCIPAL
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)

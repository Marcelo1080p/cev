from random import randint
from time import sleep
lista = list()
jogos = list()
print('='*30)
print('       JOGA NA MEGA SENA       ')
print('='*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1

while tot <= quant:

    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print('='*6, f'Sorteando {quant} Jogos', '='*6)
for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i+1}:{l}')
print('='*8, '<BOA SORTE>', '='*8)
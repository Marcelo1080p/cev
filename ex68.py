from random import randint
v = 0
while True:
   jogador = int(input('Diga um valor: '))
   computador = randint(0, 10)
   total = (jogador + computador)
   tipo = ' '
   while tipo not in 'PI':
      tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
   print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}')
   print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
   if tipo == 'P':
      if total % 2 == 0:
         print('Você Ganhou!')
         v += 1
      else:
         print('Você PERDEU!')
         break
   elif tipo == 'I':
      if total % 2 == 1:
         print('Você GANHOU!')
      else:
         print('Você PERDEU!')
         break
   print('Vamos Jogar novamente...')
print(f'GAME OVER! Você Venceu {v} Vezes.')

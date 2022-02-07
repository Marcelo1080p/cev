times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthias',
         'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos',
         'Ceará SC', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá',
         'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')
print('='*30)
print(f'Lista de times do Brasileirão: {times}')
print('='*30)
print(f'Os 5 Primeiros São {times[0:5]}')
print(f'Os últimos 4 colocados são {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'A posição do time Chapecoense é {times.index("Chapecoense")+1}ª')

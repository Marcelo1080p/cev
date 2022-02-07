frase = str(input('Digite algo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O INVERSO DE {} É {}'.format(junto, inverso ))
if inverso == junto:
    print('TEMOS UM PALÍNDROMO!')
else:
    print('A FRASE DIGITADA NÃO É UM PALÍNDROMO!')
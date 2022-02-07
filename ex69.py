tot18 = toth = totm = 0
while True:
    print('-=-'*8)
    print('CADASTRE UMA PESSOA')
    print('-=-'*8)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
            break
print(f'Total de pessoas com mais de 18 anos, {tot18} pessoas')
print(f'Ao todo temos {toth} homens cadastrados')
print(f'Ao todo temos {totm} mulheres menores de 20 anos!')
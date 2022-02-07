from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    data = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - data
    if idade <=20:
        totmenor += 1
    else:
        totmaior += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menor de idade'.format(totmenor))
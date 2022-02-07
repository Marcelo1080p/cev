list = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        list[0].append(valor)
    else:
        list[1].append(valor)
print('='*50)
list[0].sort()
list[1].sort()
print(f'Os valores pares digitados foram:  {list[0]}')
print(f'Os valores ímpares digitados foram {list[1]}')

matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz2[l][c] = int(input(f'Digite um valor para a posição {l,c}: '))
print('='*50)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz2[l][c]:^5}]', end='')
        if matriz2[l][c] % 2 == 0:
            spar += matriz2[l][c]
    print()
scol = matriz2[0][2] + matriz2[1][2] + matriz2[2][2]
print(f'A soma dos valores pares é {spar}')
print(f'A soma da terceira coluna é {scol}')
print(f'O maior valor da segunda linha é {max(matriz2[1])}')






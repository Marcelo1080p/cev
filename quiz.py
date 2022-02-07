print('-=-'*20)
print('{:-^60}'.format('BEM VINDO AO QUIZ!'))
print('-=-'*20)
jogador = str(input('Digite o seu Apelido: '))
while True:
    print('+-+'*11)
    print('Qual é o nome da mãe do Marcelo?')
    print('''
    [ 1 ] Ziza da cunha
    [ 2 ] Luzia Cunha
    [ 3 ] Luiza Cunha''')
    resp = str(input('Qual é a opção correta? '))
    if resp == 2:
        print('Parabéns você acertou!')
    elif resp == 1:
        print('Você não conhece o marcelo muito bem não é mesmo? :(')
        break
    elif resp == 3:
        print('Você não conhece o marcelo muito bem não é mesmo? :(')
        break

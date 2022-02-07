c = ('\033[m',      # 0- sem cores
    '\033[0;30;41m' # - vermelho
    );
def ajuda(com):
    help(com)


def título(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print(c[0], end='')


#Programa principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)

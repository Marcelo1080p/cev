def escreva(msg):
    tam = len(msg) + 4
    print('\033[35m~\033[m'*tam)
    print(f'  {msg}')
    print('\033[35m~\033[m'*tam)


#PROGRAMA PRINCIPAL
escreva('Marcelo Junior')
escreva('Marcelo Cordeiro Dos Santos Junior')
escreva('IRONIA XD')
 
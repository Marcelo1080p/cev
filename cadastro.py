produtos = dict()
def add_produto(c, n):
    produtos.update({c : n})


#PROGRAMA PRINCIPAL

while True:
    print('''
    [ 1 ] Adicionar Novo Produto
    [ 2 ] Consultar Produtos
    [ 3 ] Deletar Produto
    [ 4 ] Sair''')
    opcao = int(input('Informe a opção Desejada: '))
    if opcao == 1:
        nome = str(input('Nome do Produto: ')).capitalize()
        codigo = int(input('Código do Produto: '))
        add_produto(codigo, nome)
    elif opcao == 2:
        for k, v in produtos.items():
            print(f'Produto: {k}, com o código: {v}')
    elif opcao == 3:
        prod = int(input('Digite o Código do Produto Para deletar: '))
        del(produtos[int(prod)])
    elif opcao == 4:
        break
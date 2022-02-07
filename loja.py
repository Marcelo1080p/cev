marcas = dict()
funcionarios = dict()
def add_funcionarios(m, n, s):
    funcionarios.update({m and n: s})

#GERENCIAMENTO DE FUNCIONÁRIOS
while True:
    print('''
[ 1 ] Ver informações dos Funcionários
[ 2 ] Cadastrar Novo Funcionário
[ 3 ] Excluir Funcionário   ''')
    dados = str(input('Informe a opção desejada: '))
    if dados == 1:
        for m, n, s in funcionarios.items():
            print(f'Colaborador {n}, com a Matricula: {m}, tem o salário de {s}R$')
    if dados == 2:
        nome = str(input('Nome do Colaborador: '))
        matricula = int(input(f'Insira a Matricula do Colaborador {nome}: '))
        salario = float(input('Salário do Colaborador R$: '))
        funcionarios(matricula, nome, salario)

def add_marcas(c, m):
    marcas.update({c : m})


#GERENCIAMENTO DE MARCAS
while True:
    print('\033[36m-\033[m'*30)
    print(f'\033[35m{"Gerenciador de Marcas":^30}\033[m')
    print('\033[36m-\033[m' * 30)
    print('''\033[97m
[ 1 ] Cadastrar Marcas
[ 2 ] Ver Marcas Cadastradas
[ 3 ] Exluir Marca\033[m''')
    opcao = int(input('\033[97mInforme a opção desejada:\033[m '))
    print('\033[36m-\033[m' * 30)
    if opcao == 1:
        m = str(input('\033[97mNome da Marca:\033[m ')).upper()
        c = int(input('\033[97mCódigo da Marca:\033[m '))
        add_marcas(c, m)
    elif opcao == 2:
        for k, v in marcas.items():
            print(f'\033[97m{"ESSES SÃO OS PRODUTOS CADASTRADOS!":^30}\033[m')
            print(f'\033[97mMarca: {v}, tem o código: {k}\033[m')
    elif opcao == 3:
        excluir = int(input('\033[97mInsira o Código do Produto Para Exclui-lo: \033[m'))
        del(marcas[int(excluir)])
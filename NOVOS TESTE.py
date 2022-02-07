nome = str(input('Digite o seu nome: '))
if nome.isdigit():
    print('Caracter invalido')
    exit('Seu nome não pode ter caracteres especias')
print(nome)
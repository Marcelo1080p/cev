import funcoes


contatos= {
    "juliana miranda": {
        "nome": "Juliana miranda",
        "telefone": "1324414",
        "email": "juliana@gmail.com"
    },
    "caio": {
            "nome": "caio",
            "telefone": "12344",
            "email": "caio@gmail.com"
    },
    "fernando": {
            "nome": "fernando",
            "telefone": "25331334",
            "email": "fernado@gmail.com"
    }
}
comando = 0
while comando != "sair":
    comando  = input("Digite o comando: (Novo, pes, sair):")

    if comando == "novo":
        nome = input('Nome: ').strip()
        telefone = input('Telefone: ').strip()
        email = input('E-main: ').strip()

        contatos[nome.lower()] = {
            "nome": nome,
            "telefone": telefone,
            "email": email
        }
    if comando == "pes":
        nome = input("nome: ").lower()
        chaves_encontradas = funcoes.procura_chaves(contatos, nome)
        print(contatos)

        for chave in chaves_encontradas:
            print(contatos[chave])
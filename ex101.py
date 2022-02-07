def voto():
    from datetime import date
    hoje = date.today().year
    total = hoje - idade
    if total < 16:
        return print(f'A Pessoa te {total} anos, Voto negado')
    elif 16 <= total <= 18 or total >65:
        return print(f'A Pessoa tem {total} anos, VOTO Opcional!')
    else:
        return print(f'A pessoa tem {total} anos, Voto Obrigatório')


#Programa Principal
idade = int(input('Informe o seu ano de nascimento: '))
voto()

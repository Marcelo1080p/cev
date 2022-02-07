sexo = str(input('Informe o seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'FM':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo:')).strip().upper()[0]
print('Sexo {} registrado com SUCESSO!'.format(sexo))
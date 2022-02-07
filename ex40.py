print('Digite a nota do aluno abaixo Para ver a média')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando {} e {}, a média é {}'.format(nota1, nota2, média))
if média <= 4:
    print('Aluno Reprovado!')
elif média <= 6.9:
    print('Aluno ficou de RECUMPERAÇÃO!')
elif média >= 7:
    print('Aluno APROVADO!')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

média = (nota2 + nota1) / 2

if média >= 6:
    print('Aluno aprovado com média {}'.format(média))
elif 6 > média > 5:
    print('Aluno em recuperação com nota {}'.format(média))
elif média < 5:
    print('Aluno em recuperação com méda {}'.format(média))

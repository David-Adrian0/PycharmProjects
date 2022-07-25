from datetime import *

nome = str(input('Nome completo: ')).upper()
atual = datetime.today().year
nasc = int(input('Ano de nascimento: '))

if atual - nasc < 18:
    print('Infelizmente constatamos no sistema que {} não possui 18 anos, infelizmente seu alistamento foi NEGADO!'.format(nome))
    print('''
    NOME: {}
    ANO DE NASCIMENTO: {}
    SITUAÇÃO NO SISTEMA: NEGADO
    '''.format(nome, nasc))
elif atual - nasc == 18:
    print('Nosso sistema analisou que {} possui 18 anos, e está APROVADO para seu alistamento militar.'.format(nome))
    print('''
    NOME: {}
    ANO DE NASCIMENTTO: {}
    SITUAÇÃO NO SISTEMA: APROVADO'''.format(nome, nasc))
elif atual - nasc > 18:
    print('Analisamos em nosso sistema e constatamos que {} tem mais de 18 e deve se alistar IMEDIATAMENTE'.format(nome))
    print(
    '''
    NOME: {}
    ANO DE NASCIMENTO: {}
    SITUAÇÃO NO SISTEMA: EM PENDÊNCIA
    '''.format(nome, nasc))

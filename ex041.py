import datetime
from datetime import *

nome = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
hoje = datetime.today().year
idade = hoje - nasc
if idade <= 9:
    print('{} tem {} anos, então classificado na categoria MIRIN.'.format(nome, idade))
elif idade <= 14:
    print('{} tem {} anos, então classificado na categoria INFANTIL.'.format(nome, idade))
elif idade <= 19:
    print('{} tem {} anos, então classificado na categoria JÚNIOR.'.format(nome, idade))
elif idade <= 25:
    print('{} tem {} anos, então classificado na categoria SÊNIOR.'.format(nome, idade))
elif idade > 25:
    print('{} tem {} anos, então classificado na categoria MASTER.'.format(nome, idade))

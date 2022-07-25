'''nome = str(input('Nome: '))
sexo = str(input('Sexo [M/F]: ')).upper()
while not sexo == 'M' and not sexo == 'F':
    print('Digite novamente')
    sexo = str(input('Sexo [M/F]: ')).upper()
    if sexo == 'M' or 'F':
        print('Fim')'''

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Por favor, informe novamente seu sexo: ')).strip().upper()[0]
print('Registro feito com sucesso')
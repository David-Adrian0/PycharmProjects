cont = 0
conti = 0
conth = 0
con = 'S'

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'F' and idade < 20:
        cont += 1
    elif idade >= 18:
        conti += 1
    elif sexo == 'M':
        conth += 1
    con = ' '
    while con not in 'SN':
        con = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if con == 'N':
        break
print(f'O total de pessoas com mais de 18 anos foi {conti}\nO total de homens cadastrados foi {conti}\n'
      f'E temos {cont} mulheres com menos de 20 anos')

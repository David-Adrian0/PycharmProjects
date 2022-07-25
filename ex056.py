somaidade = 0
somamedia = 0
maioridadehomem = 0
nomevelho = ''
mulher20 = 0

for p in range(1, 5):
    print('----- {}° Pessoa -----'.format(p))
    pessoa = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = pessoa
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = pessoa
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
somamedia = somaidade / 4
print('A média das idades é de {}'.format(somamedia))
print('O nome do Homem mais velho é: {}, com {} anos!'.format(nomevelho, maioridadehomem))
if mulher20 > 1:
    print('Há apenas {} mulher menor de 20 anos'.format(mulher20))
else:
    print('O total de mulheres com menos de 20 anos é: {}'.format(mulher20))
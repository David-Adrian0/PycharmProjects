cont = barato = contador = vf = 0
nomeb = ' '
while True:
    print('-'*25)
    print(' ' * 2, 'ADRIANCODED PRODUTOS')
    print('-' * 25)
    nome = str(input('Nome do produto: '))
    preco = int(input('Preço do produto: '))
    vf += preco
    if preco >= 1000:
        cont += 1
    if contador == 1:
        barato = preco
        nomeb = nome
    if preco < barato:
        barato = preco
        nomeb = nome
    con = ' '
    while con not in 'SN':
        con = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    if con == 'N':
        break
print(f'O total da compra foi: {vf}\n'
      f'Temos {cont} produtos que custam mais de R$1.000\n'
      f'O produto mais barato foi {nomeb} que custa {barato}')

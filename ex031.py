km = float(input('Quantos quilometros você percorrerá na viagem? '))
if km >= 200:
    km = km * 0.45
    print('O preço da viagem é de R${:.2f}'.format(km))
else:
    km = km * 0.50
    print('O preço da viagem é de R${:.2f}'.format(km))
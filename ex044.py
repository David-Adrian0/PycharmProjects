preco = float(input('Preço dos produtos: R$'))
print('''
FORMAS DE PAGAMENTO

[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão

''')

opção = int(input('Qual é a opção? '))

if opção == 1:
    total = preco - (preco * 10 / 100)
elif opção == 2:
    total = preco - (preco * 5 / 10)
elif opção == 3:
    total = preco
    parcela = total * 2
    print('Sua compra parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra de {:.2f} será parcelada em {}x de {:.2f} COM JUROS'.format(preco, totparc, total))
else:
    total = 0
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))

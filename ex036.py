casa = float(input('Valor da casa: R$'))
salario = float(input('Valor do salário: R$'))
anos = int(input('Quantos anos você deseja pagar: '))
prestação = casa / (anos * 12)
mínimo = salario * 30 / 100

if prestação <= mínimo:
    print('O financiamento da casa foi APROVADO!')
    print('O final ficou: R${:.2f} por mês, durante {} anos'.format(prestação, anos))
else:
    print('Infelizmente o financiamento da casa foi NEGADO!')

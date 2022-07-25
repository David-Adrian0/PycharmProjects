#desafio 029
valor = 7
radar = float(input('Quantos Km/h você está? '))

if radar <= 80:
    print('Parabens por ser um motorista responsavel, não esqueça de não ultrapassar 80Km/h ☻')
else:
    multa = (radar-80) * valor
    print('Você foi multado!\nE deve pagar uma multa de R${:.2f}'.format(multa))

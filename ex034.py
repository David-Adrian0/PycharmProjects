salario = float(input('Qual é o seu salário? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava RS{:.2f} agora ganha R${:.2f}'.format(salario, novo))
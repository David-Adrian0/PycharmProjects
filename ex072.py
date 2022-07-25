cont = ('zero', 'um', 'dois', 'três',
        'quatro', 'cinco', 'seis', 'sete',
        'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'catorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
sn = 's'
while sn == 's':
    v = int(input('Digite um número de 0 a 20 e veja sua versão em extenso: '))
    if v < 0 or v > 20:
        print('ERRO! Digite novamente. ', end='')
    else:
        break
    sn = str(input('Deseja continuar?[S/N] '))
print(f'O número {v}, em extenso é: {cont[v]}')


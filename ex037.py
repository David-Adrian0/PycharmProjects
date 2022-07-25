num = int(input('Digite o número na base decimal: '))
con = int(input('''Escolha qual base númerica você deseja converter:
[1]Binário
[2]Hexadecimal
[3]Octal
Sua resposta: '''))

if con == 1:
    print('A conversão de {} para binário é {}'.format(num, bin(num)[2:]))
elif con == 2:
    print('A conversão de {} para Hexadecimal é {}'.format(num, hex(num)[2:]))
elif con == 3:
    print('A conversão de {} para Octal é {}'.format(num, oct(num)[2:]))
else:
    print('Opção inválida')

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
resposta = -1

while resposta != 5:
    print('O que você deseja fazer com esses valores? ')
    print('[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA')
    resposta = int(input('\n\nDigite um número congruente ao seu desejo: '.strip()))

    if resposta == 1:
        valorfinal = valor1 + valor2
        print('Você escolheu a opção SOMAR, a soma entre os valores {} e {} é {}'.format(valor1, valor2, valorfinal))
    elif resposta == 2:
        valorfinal = valor1 * valor2
        print('Você escolheu a opção MULTIPLICAR, a multiplicação entre os valores {} e {} é {}'.format(valor1, valor2, valorfinal))
    elif resposta == 3:
        if valor1 < valor2:
            print('Você escolheu a opção MAIOR. O maior valor é o número {} e o menor valor é o de número {}'.format(valor2, valor1))
        elif valor2 < valor1:
            print(f'Você escolheu a opção MAIOR. O maior valor é o número {valor1} e o menor valor é o número {valor2}')
        else:
            print('Todos os valores são iguais')
    elif resposta == 4:
        valor3 = int(input('Digite outro valor: '))
        valor4 = int(input('Digite outro valor: '))
        print('\nAgora você tem os valores {},{},{} e {}, o que deseja fazer com eles?'.format(valor1, valor2, valor3, valor4))
        print('[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA')
        resposta = int(input('\n\nDigite um número congruente ao seu desejo: '.strip()))
        if resposta == 1:
            valorfinal = valor1 + valor2 + valor3 + valor4
            print('Você escolheu a opção SOMAR, a soma entre os valores {}, {}, {} e {} é {}'.format(valor1, valor2, valor3, valor4, valorfinal))
        if resposta == 2:
            valorfinal = valor1 * valor2 * valor3 * valor4
            print('Você escolheu a opção MULTIPLICAR, a multiplicação entre os valores {}, {}, {} e {} é {}'.format(valor1, valor2, valor3, valor4, valorfinal))
        if resposta == 3:
            if valor1 > valor2 > valor3 > valor4:
                print(f'Você escolheu a opção MAIOR. O maior valor é o número {valor1} e o menor valor é o de número {valor4}')
            elif valor1 > valor3 > valor2 > valor4:
                print(f'Você escolheu a opção MAIOR. O maior valor é o número {valor2} e o menor valor é o número {valor4}')
            elif valor1 > valor4 > valor3 > valor2:
                print(f'Você escolheu a opção MAIOR. O maior valor é o número {valor3} e o menor valor é o número {valor4}')
            elif valor2 > valor4 > valor3 > valor1:
                print(f'Você escolheu a opção MAIOR. O maior valor é o número {valor4} e o menor valor é o número {valor3}')
            elif valor2 > valor3 > valor4 > valor1:
                print(f'Você escolheu a opção MAIOR. O maior valor é o número {valor4} e o menor valor é o número {valor3}')
            elif valor2 > valor1 > valor3 > valor4:
                print(f'Você escolheu a opção MAIOR. O maior valor é o número {valor4} e o menor valor é o número {valor3}')
            elif valor2 > valor4 > valor1 > valor3:
                print(f'Você escolheu a opção MAIOR. O maior valor é o número {valor4} e o menor valor é o número {valor3}')
            else:
                print('Todos os valores são iguais')


print('Fim do programa!')

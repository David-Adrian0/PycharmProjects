from random import randint

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)

print(
'''
FAÇA SUA ESCOLHA

[1]PEDRA
[2]PAPEL
[3]TESOURA

''')

jogador = int(input('Qual sua escolha? '))
#JOGADOR
if jogador == 1 and computador == 0:
    jogador = 'pedra'
    print('Você: {} // Computador: {}'.format(jogador, itens[computador]))
    print('EMPATADOS')
elif jogador == 2 and computador == 1:
    jogador = 'papel'
    print('Você: {} // Computador: {}'.format(jogador, itens[computador]))
    print('EMPATADOS')
elif jogador == 3 and computador == 2:
    jogador = 'tesoura'
    print('Você: {} // Computador: {}'.format(jogador, itens[computador]))
    print('EMPATADOS')

elif jogador == 3 and computador == 1:
    jogador = 'tesoura'
    print('Você: {} // Computador: {}'.format(jogador, itens[computador]))
    print('''
    Você venceu!
    Computador perdeu!''')
elif jogador == 2 and computador == 0:
    jogador = 'papel'
    print('Você: {} // Computador: {}'.format(jogador, itens[computador]))
    print('''
    Você venceu!
    Computador perdeu!''')
elif jogador == 1 and computador == 2:
    jogador = 'pedra'
    print('Você: {} // Computador: {}'.format(jogador, itens[computador]))
    print('''
    Você venceu!
    Computador perdeu!''')
elif jogador == 2 and computador == 2:
    jogador = 'papel'
    print('Você: {} // Computador: {}'.format(jogador, itens[computador]))
    print('''
    Você perdeu!
    Computador venceu!''')
elif jogador == 1 and computador == 1:
    print('Você: {} // Computador: {}'.format(jogador, itens[computador]))
    print('''
    Você perdeu!
    Computador venceu!''')
elif jogador == 3 and computador == 0:
    print('Você: {} // Computador: {}'.format(jogador, itens[computador]))
    print('''
    Você perdeu!
    Computador venceu!''')
else:
    print('OPÇÃO INVÁLIDA')
#COMPUTADOR
'''if computador == 2 and jogador == 2:
    jogador = 'papel'
    print('Você: {} // Computador: {}'.format(jogador, itens[computador]))
    print('Computador venceu!')
elif computador == 1 and jogador == 1:
    jogador = 'pedra'
    print('Você: {} // Computador: {}'.format(jogador, itens[computador]))
    print('Computador venceu!')
elif computador == 0 and jogador == 3:
    jogador = 'tesoura'
    print('Você: {} // Computador: {}'.format(jogador, itens[computador]))
    print('Computador venceu!')'''

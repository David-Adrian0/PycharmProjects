#import
from random import randint
from time import sleep

#variáveis
computador = randint(0, 10)
acertos = False
pontopc = 0
pontojog = 0

#While
while not acertos:
    jogador = int(input('Qual é o seu palpite? '))
    pontopc += 1
    if jogador == computador:
        pontojog += 1
        acertos = True
    else:
        if jogador < computador:
            print('Analisando...')
            sleep(2)
            print('Aumente seu valor!')
        elif jogador > computador:
            print('Analisando...')
            sleep(2)
            print('Reduza o seu valor!')

print('Acertou! {} quantidades de tentativas e {} acerto'.format(pontopc, pontojog))

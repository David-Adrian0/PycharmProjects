from random import randint
tipo = ''
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = str(input('Par ou Impar?[P/I] ').upper().strip()[0])
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar?[P/I] ').upper().strip()[0])
    print(f'Você jogou {jogador} e o computador jogou {computador}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!!!')
            v += 1
        else:
            print('Você perdeu!!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!!!')
            v += 1
        else:
            print('Você perdeu!!!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')

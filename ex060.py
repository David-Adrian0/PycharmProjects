print('Digite um valor e veja o seu fatorial')
num = int(input('\nDigite um valor: '))
cont = num
fat = 1

while cont > 0:
    print(f'{cont}', end='')
    fat *= cont
    cont -= 1
    print(' X ' if cont > 0 else ' = ', end='')
print(f'{fat}')
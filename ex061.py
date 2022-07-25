termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
cont = termo

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')

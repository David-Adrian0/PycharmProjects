valor = list()
par = list()
impar = list()
while True:
    valor.append(int(input('Digite um valor: ')))
    r = str(input('Deseja continuar?[S/N] ').upper().strip())
    if r in 'N':
        break
for i, c in enumerate(valor):
    if c % 2 == 0:
        par.append(c)
    elif c % 2 >= 1:
        impar.append(c)
print(f'Lista completa: {valor}')
print(f'Lista com números pares: {par}')
print(f'Lista com números ímpares: {impar}')

cont = 0
par = 0
for v in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        num += num
        cont += 1
print('''
        Quantidade de números pares: {}
        Soma dos pares: {}'''.format(cont, par))
valor = list()
for núm in range(0, 5):
    n = int(input('Digite um valor: '))
    if núm == 0 or n > valor[-1]:
        valor.append(n)
        print('Adicionando o valor na posição 0...')
    else:
        pos = 0
        while pos < len(valor):
            if n <= valor[pos]:
                valor.insert(pos, n)
                print(f'O valor foi inserido entre {pos} e {n}')
                break
            pos += 1
print(valor)

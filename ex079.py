valor = list()
r = ''
while True:
    n = int(input('Digite um valor: '))
    if n not in valor:
        valor.append(n)
        r = str(input('Valor adicionado com sucesso!\nGostaria de continuar?[S/N] '))
        if r in 'Nn':
            break
    else:
        print('Esse valor já foi adicionado, não será adicionado!')
print(f'A lista em ordem crescente é: {sorted(valor)}\nLista orginal: {valor}')

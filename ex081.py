valor = list()
while True:
    valor.append(int(input('Digite um valor: ')))
    r = str(input('Deseja continuar?[S/N] ').upper().strip())
    if r == 'N':
        break
print(f'A lista original é: {valor}\nA quantidade de elementos dentro da lista é de: {len(valor)}')
valor.sort(reverse=True)
print(f'A lista ordenada do maior para o menor é: {valor}')
if 5 in valor:
    print('O valor 5 está na lista')
else:
    print('Não foi possível fazer a leitura do número 5 dentro da lista')

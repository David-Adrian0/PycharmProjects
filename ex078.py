valor = []
for pos in range(0, 5):
    valor.append(int(input(f'Digite um valor para a posição {pos}: ')))
print(f'Você digitou os valores {valor}')
print(f'As posições de maior e menor valor são: {sorted(valor)}')


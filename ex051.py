inicio = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = 10
quantidadedetermo = termo
for repetição in range(inicio, quantidadedetermo+1, razão):
    print(repetição, end=' -> ')
print('FIM')

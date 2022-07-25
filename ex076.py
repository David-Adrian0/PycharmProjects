print('*' * 30, '\nLISTAGEM DE PRODUTOS E PREÇOS')
print('*' *30)

print('=-=' * 13)

listagem = ('Notebook', 1.659,
            'Ipad', 3.800,
            'Caderno', 27.8,
            'Livro', 10,
            'Capinha de Celular', 28.65,
            'Celular', 600)
for produtos in range(0, (len(listagem))):
    if produtos % 2 == 0:
        print(f'{listagem[produtos]:.<30}', end='')
    else:
        print(f'R${listagem[produtos]:.3f}')
print('=-=' * 13)

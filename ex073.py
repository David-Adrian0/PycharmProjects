lista = ('América-MG', 'Athletico-PR', 'Atlético-GO',
         'Atlético-MG', 'Avaí', 'Botafogo',
         'Bragantino', 'Ceará', 'Corinthians',
         'Coritiba', 'Cuiabá', 'Flamengo',
         'Fluminense', 'Fortaleza', 'Goiás',
         'Internacional', 'Juventude', 'Palmeiras',
         'Santos', 'São Paulo')
print(f'Lista de times do Brasileirão: {lista}')
print(f'Os 5 primeiros colocados são: {lista[0:5]}')
print(f'Os 4 últimos são: {lista[-4:]}')
print(f'Os times em ordem alfabética são: {sorted(lista)}')
print(f'O Flamengo está na posição: {lista.index("Flamengo")+1}')

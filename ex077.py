p = ('celular', 'arroz', 'tesoura', 'tablet', 'notebook', 'caderno', 'aprender')

for palavra in p:
    print(f'\nAs sílabas encontradas na palavra {palavra.upper()} foram ', end='')
    for s in palavra:
        if s.lower() in 'aeiou':
            print(s, end=' ')

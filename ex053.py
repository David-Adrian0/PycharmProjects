frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print(junto, inverso)
    print('Temos um PALÍNDROMO')
else:
    print(junto, inverso)
    print('Não temos um PALÍNDROMO')
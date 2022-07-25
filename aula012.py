#condição simples > if and else
#condição aninhada > if, elif and else
'''from time import sleep
h1 = str(input('nome: ')).upper()

if h1 == 'David'.upper():
    print('Olá, fofenhooooooooo')
elif h1 == 'Te odeio'.upper():
    print('Te perguntei alguma coisa? ')
elif h1 == 'Te amo'.upper():
    sleep(3)
    print('Ain... tô com vecoinha 🥰')
else:
    print('Mal educado!')'''

print('=-=-'*10)
print('Teste de conversão Decimal para Binária')
print('=-=-'*10)

num = int(input('Digite o número: '))

numb = num % 2
numd = num // 2

print(f'O valor da divisão foi {numd}')

numd1 = numd // 2
numb1 = numd % 2

print(f'a divisão de {numd} por 2 foi: {numd1}')

lista = [numb1, numb]

print(f'O resto da divisão foi {numb} e {numb1}, portanto\nO número {num}, na base Binária tem o valor de: {lista}')

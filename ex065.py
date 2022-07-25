v1 = 0
cont = 0
maior = 0
menor = 0
c = ''
while c != 'n'.upper():
    v = int(input('Digite um valor: '))
    v1 += v
    cont += 1
    if cont == 1:
        maior = menor = v
    else:
        if cont > 1:
            maior = v
        if cont < menor:
            menor = v
    c = str(input('Deseja continuar?[S/N] ')).upper()
vm = v1/cont
print('A soma de todos os valores é {}'.format(v1))
print('A média dos valores é: {}'.format(vm))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))

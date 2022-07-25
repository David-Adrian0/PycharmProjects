num = 0
cont = 0
while num != 999:
    num = int(input('Digite um número: '))
    cont += 1
    if num == 999: print('Fechando o programa')
print('Você digitou o número 999, chegando ao fim do programa\nAo todo você digitou {} valores.'.format(cont))

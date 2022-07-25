v = 0
v1 = 0
cont = 0
while v != 999:
    v = int(input('Digite um valor [DIGITE 999 PARA PARAR]: '))
    if v == 999:
        break
    v1 += v
    cont += 1
print(f'Foram digitados {cont} valores e a soma entre eles é {v1}')
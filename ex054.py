from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(pess)))
    idade = atual - nasc

    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas de maior de idade e {} pessoas de menor de idade'.format(totmaior, totmenor))
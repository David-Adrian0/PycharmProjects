r1 = float(input('Digite o primeiro seguimento: '))
r2 = float(input('Digite o segundo seguimento: '))
r3 = float(input('Digite o terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('Podemos obter um triangulo!')
else:
    print('Não se pode obter um triangulo')
núm = (int(input('Digite um valor: ')),
     int(input('Digite outro valor: ')),
     int(input('Digite mais um valor: ')),
     int(input('Digite um útimo valor: ')))

print(f'Você digitou os valores {núm}')
print(f'O número 9 apareceu {núm.count(9)} vezes')
if 3 not in núm:
     print('Infelizmente não foi possivel fazer a leitura do número 3')
else:
     print(f'O valor 3 se enccontra na {núm.index(3)+1}° posição')
print(f'A quantidade de números pares foi: ', end='')

for n in núm:
     if n % 2 == 0:
          print(n, end='')

'''Trabalhando junto com o Professor'''

num = int(input('Informe uma sequencia númerica: '))
n = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
dm = num // 10000 % 10

print('Analisando o número...'.format(num))
print('Unidade: {}'.format(n))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Minlhar: {}'.format(m))
print('Dezena de Milhar: {}'.format(dm))

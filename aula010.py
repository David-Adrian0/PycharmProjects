'''Contições'''
#exeplo

tempo = int(input('Quantos anos o seu carro tem? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Tá na hora de trocar!!!')
print('--FIM--')

#exemplo aula prática

nome = str(input('Qual é o seu nome? '))
if nome == 'David':
    print('Que nome lindo!!')
else:
    print('Seu nome é tão normal')
print('Bom dia, {0}'.format(nome))

#exemplo aula prática

n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite sua nota: '))
m = (n1+n2)/2
if m <= 6.0:
    print('Tá na média mas podia ser melhor...')
else:
    print('Miserável quem te ensinou? :O')
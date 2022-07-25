'''nome = str(input('Digite seu nome: '))

print('\nSeu nome maiúsculo é:', nome.upper())
print('\nSeu nome minúsculo é:', nome.lower())
print('\nSeu nome sem espaços na direita é:', nome.rstrip())
print('\nSeu nome sem espaços na esquerda é:', nome.lstrip())

pnome = nome[0:5]

print('\nO primeiro nome caracterizado como:', nome[0:5], '\nContém', len(pnome),'caracteres inseridos')'''

'''Forma do professor'''

nome = str(input('Digite seu nome: '))
print('\nAnalizando seu nome...')
print('\nSeu nome em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome em minúsculo é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

separa = nome.split()

print('\nSeu nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

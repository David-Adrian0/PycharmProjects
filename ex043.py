peso = float(input('Peso: '))
altura = float(input('Altura: '))

IMC = peso / (altura**2)

if IMC < 18.5:
    print('[IMC: {:.1f}]\nABAIXO DO PESO'.format(IMC))
elif IMC >= 18.5 or IMC < 25:
    print('[IMC: {:.1f}]\nPESO IDEAL'.format(IMC))
elif IMC >= 25 or IMC < 30:
    print('[IMC: {:.1f}]\nSOBREPESO'.format(IMC))
elif IMC >= 30 or IMC < 40:
    print('[IMC: {:.1f}]\nOBESIDADE'.format(IMC))
elif IMC >= 40:
    print('[IMC: {:.1f}]\nOBESIDADE MÓRBIDA'.format(IMC))

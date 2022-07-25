lado1 = float(input('Digite o primeiro lado do triângulo: '))
lado2 = float(input('Digite o segundo lado do triângulo: '))
lado3 = float(input('Digite o terceiro lado do triângulo: '))

#ESCALENO
if lado1 != lado2 != lado3:
    print('ESCALENO')
elif lado2 != lado1 != lado3:
    print('ESCALENO')
elif lado3 != lado2 != lado1:
    print('ESCALENO')

#ISÓSCELES
elif lado1 != lado2 and lado3:
    print('ISÓSCELES')
elif lado2 != lado1 and lado3:
    print('ISÓSCELES')
elif lado3 != lado2 and lado1:
    print('ISÓSCELES')

#EQUILÁTERO
elif lado1 == lado2 and lado3:
    print('EQUILÁTERO')

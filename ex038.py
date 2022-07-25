num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

if num1 > num2:
    print('O maior número é {} e o menor é {}'.format(num1, num2))
elif num1 == num2:
    print('Os valores {} e {} são iguais'.format(num1, num2))
elif num1 < num2:
    print('O maior número é {} e o menor é {}'.format(num2, num1))

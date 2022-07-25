express = list()
v = str(input('Digite uma expressão qualquer: '))
for s in express:
    if v == '(':
        express.append('(')
    elif v == ')':
        if len(express) > 0:
            express.pop()
        else:
            break
if len(express) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')

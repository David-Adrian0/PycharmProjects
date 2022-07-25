from random import randint
n = (randint(1, 10), randint(1,10), randint(1,10),
     randint(1,10), randint(1,10))

print(f'Os valores sorteados foram: {n}')
print(f'O maior valor é: {max(n)} e o menor valor é: {min(n)}')

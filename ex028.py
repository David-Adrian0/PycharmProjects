import random
from time import sleep

num = [0, 1, 2, 3, 4, 5]
num = random.randint(0,5)

r = int(input('Qual número eu pensei? '))
print('Procesando...')
sleep(3)
if r == num:
    print('Miserável, quem te ensinou? :O')
else:
    print('Sou mais esperto, ganhei de você, humano tolo!')
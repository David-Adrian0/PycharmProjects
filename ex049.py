num = int(input('Qual número da tabuada você quer? '))
for tab in range(0, 11):
    print('{} + {:2} = {}'.format(num, tab, tab+num))

#minha forma de fazer:
'''nc = str(input('Digite o nome da sua cidade: '))

if nc == 'Santo':
    print('Aprovado')
else:
    print('Reprovado')'''

#Forma do Professor:
cid = str(input('Em que cidade você nasceu? '))
print(cid[:5].upper() == 'SANTO')

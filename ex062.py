print('Bem-vindo ao gerador de PA')
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
termos = 11
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= termos:
        print('{} -> '.format(primeiro), end='')
        primeiro += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você deseja exibir a mais? '))
    if mais > 0:
        termos += mais
print('FIM!\nProgressão finalizada com {} termos mostrados'.format(total))

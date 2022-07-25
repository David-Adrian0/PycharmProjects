vp = 0
rsp = ''
v = int(input('Digite um valor para a tabuada aparecer: '))
for c in range(0, 10 + 1):
    vf = vp * v
    print(f'{vp} x {v} = {vf}')
    vp += 1
rsp = str(input('Deseja continuar?[S/N] ')).upper().strip()
while rsp == 'S':
    vp = 0
    v = int(input('Digite um valor para a tabuada aparecer: '))
    if v < 0:
        break
    for c in range(0, 10 + 1):
        vf = vp * v
        print(f'{vp} x {v} = {vf}')
        vp += 1
    rsp = str(input('Deseja continuar?[S/N] ')).upper().strip()
print('Fim do programa')

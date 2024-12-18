from random import randint
from time import sleep

print('-' * 30)
print(f'{"JOGO da MEGA SENA":^30}')
print('-' * 30)
jogosNum = int(input('Quantos jogos você quer fazer? '))
print('-' * 30)
jogos = []
for c in range(0,jogosNum):
    jogos.append([])
    for d in range(0,6):
        while True:
            num = randint(1,60)
            if num not in jogos[c]:
                jogos[c].append(num)        # gastei uns 40 minutos até perceber que tinha colado outro randint() aqui
                break
print(f'{"Jogos Sorteados:":^30}')
for c in range(0,jogosNum):
    sleep(0.4)
    print(f'Jogo nº{c+1:2}:   ', end='')
    jogos[c].sort()
    sleep(0.4)
    for d in range(0, 6):
        if d == 5:
            print(f'{jogos[c][d]:2}', end='')
        else:
            print(f'{jogos[c][d]:2}, ', end='')
    print()
#for num, jogo in enumerate(jogos):         # também dava para ter feito assim, mas eu quis formatar
#print(f'Jogo nº{num+1:2}: {sorted(jogo)}')
#print(jogos)
print('-' * 30)
print(f'{"BOA SORTE":^30}')

# guanabara

lista = list()
jogos = list()
print('-' * 30)
print(f'{"JOGO da MEGA SENA":^30}')
print('-' * 30)
quant = int(input('Quantos jogos você quer fazer? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-' * 3, f' Sorteando {quant} jogos ', '-' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-' * 5, ' Boa Sorte! ', '-' * 5)

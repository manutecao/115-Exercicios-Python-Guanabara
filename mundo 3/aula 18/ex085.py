principal = [[],[]] # indíce 0 == pares     índice 1 == ímpares
for c in range(1,8):    # podia usar o c com o range(1,8) já que não vou utilizá-lo para indicar índice
    num = int(input(f'Digite o {c}º número: '))     # logo, aqui não precisa de +1
    if num % 2 == 0:
        principal[0].append(num)
    else:
        principal[1].append(num)
"""print(f'Números pares: {sorted(principal[0])}')     # ele disse MOSTRAR em ordem crescente
print(f'Números ímpares: {sorted(principal[1])}')"""
principal[0].sort()     # mas acabou alterando a ordem na fonte
principal[1].sort()
print(f'Números pares: {principal[0]}')
print(f'Números ímpares: {principal[1]}')

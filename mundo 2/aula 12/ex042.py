r = [1, 2, 3]
for c in range(0,3):
    r[c] = float(input(f'Digite o comprimento do {c+1}º segmento: '))

if (r[0] + r[1] > r[2]) and (r[1] + r[2] > r[0]) and (r[0] + r[2] > r[1]):
    print('Sim, esses segmentos podem format um triângulo ', end='')
    if r[0] == r[1] == r[2]:
        print('Equilátero.')
    elif r[0] != r[1] != r[2] != r[0]:
        print('Escaleno.')
    # elif (r[0] == r[1]) or (r[0] == r[2]) or (r[1] == r[2]):                          # errado
    # elif (r[0] == r[1] != r[2]) or (r[0] == r[2] != r[1]) or (r[1] == r[2] != r[0]):  # correto
    else:                                                                               # correto simplificado
        print('Isóceles')
else:
    print('Rola não pae.')

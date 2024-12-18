# ele não mostrou matrizes ainda, vou fazer cada linha em uma lista então
"""linha = []
linha2 = []
linha3 = []
for c in range(0,3):
    linha.append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(0,3):
    linha2.append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(0,3):
    linha3.append(int(input(f'Digite um valor para [2, {c}]: ')))
print('-' * 30)
for ind in linha:
    print(f'[  {ind}  ]', end='')
print()
for ind in linha2:
    print(f'[  {ind}  ]', end='')
print()
for ind in linha3:
    print(f'[  {ind}  ]', end='')"""

# esse aqui era ao jeito certo
matriz = []   # [x][y]    X é a linha,    Y é a colun
for c in range(0,3):
    matriz.append([])
    for d in range(0,3):
        matriz[c].append(int(input(f'Digite um valor para [{c}, {d}]: ')))
print('-' * 30)

for c in range(0,3):
    for d in range(0,3):
        print(f'[{matriz[c][d]:^5}]', end='')
    print()

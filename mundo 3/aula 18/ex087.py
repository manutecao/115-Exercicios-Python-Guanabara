# tenho a impressão que terei que refazer tudo
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
    print(f'[  {ind}  ]', end='')
print('\n', '-' * 30)

soma = 0
for ind in linha:
    if ind % 2 == 0:
        soma += ind
for ind in linha2:
    if ind % 2 == 0:
        soma += ind
for ind in linha3:
    if ind % 2 == 0:
        soma += ind
print(f'A soma de todos os valore pares é {soma}.')

terceiraCol = linha[2] + linha2[2] + linha3[2]
print(f'A soma dos valores da terceira coluna é {terceiraCol}.')

maior = 0
for c, d in enumerate(linha2):
    if c == 0:
        maior = d
    elif d > maior:
        maior = d
print(f'O maior número da segunda linha é {maior}.')"""

# esse aqui era ao jeito certo
matriz = [[], [], []]   # [x][y]    X é a linha,    Y é a colun
somaPares = somaTerc = maior = 0
for c in range(0,3):
    for d in range(0,3):
        matriz[c].append(int(input(f'Digite um valor para [{c}, {d}]: ')))
        if matriz[c][d] % 2 == 0:       # soma dos pares
            somaPares += matriz[c][d]
        if d == 2:                      # soma da coluna 3
            somaTerc += matriz[c][d]
        if c == 1 and matriz[c][d] > maior:
            maior = matriz[c][d]        # maior da linha 2
print('-' * 30)

for c in range(0,3):
    for d in range(0,3):
        print(f'[{matriz[c][d]:^5}]', end='')
    print()
print('-' * 30)

"""soma = 0
for c in range(0,3):         # também pode ser feita essa verificação na coleta no valor
    for d in range(0,3):     # não que assim esteja errado, só é bom praticar de maneiras diferentes
        if matriz[c][d] % 2 == 0:
            soma += matriz[c][d]
somaTerc = 0             # mesma coisa aqui, 
for c in range(0,3):
    somaTerc += matriz[c][2]
maior = 0                # e aqui
for c, d in enumerate(matriz[1]):
    if c == 0:
        maior = d
    elif d > maior:
        maior = d"""

print(f'A soma de todos os valore pares é {somaPares}.')
print(f'A soma dos valores da terceira coluna é {somaTerc}.')
print(f'O maior número da segunda linha é {maior}.')

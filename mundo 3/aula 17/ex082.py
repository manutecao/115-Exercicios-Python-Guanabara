lista = []
esc = ' '
while esc not in 'N':
    lista.append(int(input('Digite um número: ')))
    esc = ' '
    while esc not in 'SN':
        esc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if esc not in 'SN':
            print('Opção inválida. ', end='')
pares = []      # lista = lista2 = []  isso cria um link entre as duas listas, devo iniciá-las separadamente.
impares = []
for item in lista:
    if item % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)
print(f'A lista original é: {lista}')
print(f'A lista com os valores PARES é: {pares}')
print(f'A lista com os valores ÍMPARES é: {impares}')

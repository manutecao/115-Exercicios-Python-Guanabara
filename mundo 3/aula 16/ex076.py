# minha versão
lista = ('Caneta', 1, 'Caderno', 14, 'Lapiseira', 3.60, 'Folha A4', 8.99 )
print('{:^25}'.format('Lista de produtos'))
print('-' * 25)
for posi, item in enumerate(lista):
    if posi % 2 == 0:
        print(f'{item:.<15} ', end='')
    else:
        print(f'R$ {lista[posi]:>6.2f}')
print('-' * 25)

# guanabara alternativo
lista2 = ('Caneta', 1, 'Caderno', 14, 'Lapiseira', 3.60, 'Folha A4', 8.99 )
print('{:^25}'.format('Lista de produtos'))
print('-' * 25)
for item in range(0, 7, 2): #   '7' pois o último item está na posição 6, logo, 6 seria ignorado
#for item in range(0, len(lista2), 2):     #   eu não percebi que poderia ter utilizado o 'for' com um 'range'
    print(f'{lista2[item]:.<15} ', end='')
    print(f'R$ {lista2[item + 1]:>6.2f}')
print('-' * 25)

# guanabara
lista3 = ('Caneta', 1, 'Caderno', 14, 'Lapiseira', 3.60, 'Folha A4', 8.99 )
print(f'{"Lista de produtos":^25}')
print('-' * 25)
for pos in range(0, len(lista3)):
    if pos % 2 == 0:
        print(f'{lista3[pos]:.<15} ', end='')
    else:
        print(f'R$ {lista3[pos]:>6.2f}')
print('-' * 25)

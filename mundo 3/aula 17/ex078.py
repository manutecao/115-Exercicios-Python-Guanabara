""" minha versão
lista = list(range(0,5))
for c in range(0,5):
    lista[c] = int(input(f'Digite o valor da {c}ª posição: '))
print('Os valores digitados foram:', lista)
maior = max(lista)
print(f'O maior valor da lista é {maior} e sua aposição é a {lista.index(maior)}.')
menor = min(lista)
print(f'O menor valor da lista é {menor} e sua aposição é a {lista.index(menor)}.')

# minha versão 2
lista = list(range(0,5))
for c in range(0,5):
    lista[c] = int(input(f'Digite o valor da {c}ª posição: '))
print('Os valores digitados foram:', lista)
maior = max(lista)
print(f'O maior valor da lista é {maior} nas posições ', end='')
for c, d in enumerate(lista):
    if d == maior:
        print(c, end='... ')
menor = min(lista)
print(f'\nO menor valor da lista é {menor} nas posições ', end='')
for c, d in enumerate(lista):
    if d == menor:
        print(c, end='... ')
print('')"""

# minha versão 3
lista = []
for c in range(0,5):
    lista.append(int(input(f'Digite o valor da posição {c}: ')))
print('Os valores digitados foram:', lista)
maior = max(lista)
print(f'O maior valor da lista é {maior} nas posições ', end='')
for c, d in enumerate(lista):
    if d == maior:
        print(c, end='... ')
menor = min(lista)
print(f'\nO menor valor da lista é {menor} nas posições ', end='')
for c, d in enumerate(lista):
    if d == menor:
        print(c, end='... ')

# guanabara
lista = []
for c in range(0,5):
    lista.append(int(input(f'Digite o valor da posição {c}: ')))
    if c == 0:                          #   a únia diferença foi que ele fez a identificação do maior e menor na mão
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            manor = lista[c]
print('Os valores digitados foram:', lista)
print(f'O maior valor da lista é {maior} nas posições ', end='')
for c, d in enumerate(lista):
    if d == maior:
        print(c, end='... ')
print(f'\nO menor valor da lista é {menor} nas posições ', end='')
for c, d in enumerate(lista):
    if d == menor:
        print(c, end='... ')

# minha versão
lista = list()
for c in range(0,5):
    num = int(input('Digite o número: '))
    ind = 0
    while ind < len(lista):     # este téste lógico impede que o looping infinito na condicional abaixo
        if lista[ind] < num:    # avança o index até que:
            ind += 1
        elif lista[ind] == num: # o valor da posição atual seja igual ao número digitado
            ind += 1
            break
        elif lista[ind] > num:  # ou o valor da posição ser menor que o número digitado
            break
    if ind == len(lista):
        print('Adicionado na última posição...')
    else:
        print(f'Adicionado na posição {ind}.')
    lista.insert(ind, num)
print(lista)
del lista

# guanabara
lista = list()
for c in range(0,5):
    num = int(input('Digite o número: '))
    if c == 0 or num > lista[-1]:   # mais fácil do que usar 'elif num > lista[len(lista) - 1]:'
        lista.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos}.')
                break
            pos += 1
print('-' * 30)
print(f'Os valores digitados em ordem foram {lista}.')

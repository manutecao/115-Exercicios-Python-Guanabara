# minha versão
lista = []
esc = ' '
contador = 0
while esc not in 'N':
    lista.append(int(input('Digite um número: ')))
    contador += 1
    esc = ' '
    while esc not in 'SN':
        esc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if esc not in 'SN':
            print('Opção inválida. ', end='')
print(f'Ao total foram digitados {contador} números.')
print(f'A lista em ordem decrescente é: {sorted(lista, reverse=True)}.')
if 5 in lista:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
del lista

# guanabara
lista = []
contador = 0
while True:
    lista.append(int(input('Digite um número: ')))
    contador += 1
    esc = ' '
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-' * 30)
print(f'Ao total foram digitados {contador} números.')
print(f'A lista em ordem decrescente é: {sorted(lista, reverse=True)}.')
if 5 in lista:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')

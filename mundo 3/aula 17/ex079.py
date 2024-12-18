""" minha versão

lista = [0]     # gambiarra pois não soube como verificar os valores com ela vazia 'lista = []', ou 'lista = list()'
num = 1
while True:
    num = int(input('Digite um número: (0 para sair) '))    # eu fiz utilizando flags, mas ele pediu pergunta de [S/N]
    if num == 0:
        break
    else:
        digitado = False
        for c in lista:     # verifica se o número já foi digitado
            if c == num:
                print(f'Número {num } já foi digitado.')
                digitado = True
        if not digitado:
            if lista[0] == 0:   # verifica se o valor da primeira posição é 0
                lista.append(num)
                del lista[0]
            else:
                lista.append(num)
print(f'Os valores digitados em ordem crescente são {sorted(lista)}.')"""

# minha versão 2
lista2 = []
esc = ' '
while esc != 'N':
    num = int(input('Digite um número: '))
    if num in lista2:
        print('Valor duplicado, não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
        lista2.append(num)
    esc = ' '
    while esc not in 'SN':
        esc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if esc not in 'SN':
            print('Opção inválida. ', end='')
        else:
            break
print(f'Os valores digitados em ordem crescente são {sorted(lista2)}.')

# guanabara
lista2 = []
while True:
    num = int(input('Digite um número: '))
    if num not in lista2:
        lista2.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar...')
    esc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if esc in 'N':
        break
lista2.sort()
print(f'Os valores digitados em ordem crescente são {lista2}.')

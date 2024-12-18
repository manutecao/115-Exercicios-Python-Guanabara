print('-' * 20)
print('Lista de compras')
print('-' * 20)
s = mais1k = maisbaratopreco = 0
maisbaratonome = ''
#sair = False
while True:
    nome = str(input('Produto: ')).strip()      # não sei como deveria validar isso, talvez 'nome.isnum()' ?
    while True:                 # acho certo validar todas as entradas de dados vitais
        try:
            preco = float(input('Preço: R$ '))
        except ValueError:
            print('Digite o valor do produto em números inteiros ou reais.')
        else:
            if preco < 0:
                print('O preço deve ser de R$ 0,00 ou acima.')
            else:
                break

    s += preco
    if maisbaratopreco == 0 or preco < maisbaratopreco: # já que os dois blocos fazem a mesma coisa, faz-se um teste só
        maisbaratopreco = preco
        maisbaratonome = nome
    #else:                   # sem esse else, ele faz o procedimento duas vezes no primeiro ciclo
    #   if preco < maisbaratopreco:
    #       maisbaratopreco = preco
    #       maisbaratonome = nome
    if preco > 1000:
        mais1k += 1

    #while True:            eu utilizei o 'while True' em todas as situações para exercitá-lo, mesmo não sendo o ideal
    esc = ' '
    while esc not in 'NS':
        esc = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
        if esc not in 'NS':
            print('Digite uma opção válida ( S para sim, N para não)')
    #   else:
    #       if esc in 'N':
    #           sair = True
    #           break
    #       else:
    #           break
    #if sair:
    if esc == 'N':
        break

print('-' * 20)
print(f'Total gasto na compra foi de R${s:.2f}.')
print(f'Produtos que custaram mais de R$ 1000.00: {mais1k} un.')
print(f'Produto mais barato foi {maisbaratonome}, custando R$ {maisbaratopreco:.2f}.')

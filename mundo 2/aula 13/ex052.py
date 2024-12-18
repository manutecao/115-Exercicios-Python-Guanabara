num = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1, num + 1):
    #print(c, end=' ')
    if num % c == 0:
        print(f'\033[33m', end=' ')     # fiquei confuso com esse esquema de coloração
        cont += 1
    else:
        print(f'\033[31m', end=' ')
    print(c, end=' ')
#print('\n')
print(f'\033[m\nO nº {num} foi divisível por {cont} vezes, portanto, ',end='')
if cont == 2:
    print('é PRIMO.')
else:
    print('NÃO é PRIMO.')

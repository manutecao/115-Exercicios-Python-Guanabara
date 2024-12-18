from random import randint

def sorteia(lista):
    print('Soteando cinco valores para a lista:', end=' ')
    for n in range(0, 5):
        num = randint(1, 10)
        print(num, end=' ')
        lista.append(num)
    print('PRONTO!')

def somaPar(lst):
    soma = 0
    for n in lst:
        if n % 2 == 0:
            soma += n
    print(f'Somando o valores pares de {lst}, temos {soma}.')

numeros = []
sorteia(numeros)
somaPar(numeros)

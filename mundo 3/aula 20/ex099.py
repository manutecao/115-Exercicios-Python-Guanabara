# minha versão
"""from random import randint

def linha(tipo, tam):
    if tipo == 1:
        print('-' * tam)
    elif tipo == 2:
        print('-=' * tam)

def maior(lst):
    print(f'O maior número da lista é {max(lst)}.')

lista = []
for v in range(0,4):
    linha(2, 20)
    print('Analisando os valores passados...')
    qtd = randint(1, 10)
    for n in range(0, qtd):
        num = randint(1,10)
        print(num, end=' ')
        lista.append(num)
    print(f'Foram informados {len(lista)} valores ao todo')
    maior(lista)
    lista.clear()"""

# minha versão 2
"""from random import randint
from time import sleep

def linha(tipo, tam):
    if tipo == 1:
        print('-' * tam)
    elif tipo == 2:
        print('-=' * tam)

def maior():
    lista = []
    linha(2, 20)
    print('Analisando os valores passados...')
    qtd = randint(0, 10)
    for n in range(0, qtd):
        sleep(0.4)
        num = randint(1,10)
        print(num, end=' ')
        lista.append(num)
    print(f'Foram informados {len(lista)} valores ao todo')
    print(f'O maior número da lista é {max(lista)}.')
    lista.clear()

for v in range(0,4):
    maior()"""

# precisei fazer uma terceira vez porque a minha interpretação do enunciado estava errada
# minha versão 3
from time import sleep

def linha(tipo, tam):
    if tipo == 1:
        print('-' * tam)
    elif tipo == 2:
        print('-=' * tam)

def maior(*numeros):
    print('Analisando os valores passados...')
    #print(f'O maior valor entre {numeros} é {max(numeros)}') # tem que ser RAIZ :(
    mai = 0
    for n in numeros:
        sleep(0.4)
        print(n, end=' ')
        if n >= mai:
            mai = n
    print(f'Foram passados {len(numeros)} valore ao todo.')
    print(f'O maior valor entre {numeros} é {mai}')
    linha(1, 50)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

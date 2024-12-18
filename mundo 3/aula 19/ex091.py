from random import randint
from time import sleep

result = {}
for j in range(1,5):
    result['jogador'+f'{j}'] = randint(1, 6)
print('Valores sorteados:')
for j, v in result.items():
    print(f'O {j} tirou {v}')
print('Ranking dos jogadores:')
#print(result.items())
ordenado = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
"""
dict()  transforma uma LISTA com tuplas em um DICIONÁRIO, logo:
     isso: dados1 = [('jogador1', 1), ('jogador2', 4), ('jogador3', 6), ('jogador4', 3)]
vira isso: dados2 = {'jogador1': 5, 'jogador2': 3, 'jogador3': 6, 'jogador4': 2}
        cada TUPLA dentro da Lista vira um ITEM no Dicionário,
        onde: tupla1[0] vira a CHAVE e tupla2[1] vira o VALOR de cada ITEM do Dicionário

dados.items()   transforma um DICIONÁRIO em uma LISTA com tuplas, logo:
     isso: dados1 = {'jogador1': 5, 'jogador2': 3, 'jogador3': 6, 'jogador4': 2}
vira isso: dados2 = [('jogador1', 1), ('jogador2', 4), ('jogador3', 6), ('jogador4', 3)]
        cada ITEM do dicionário vira uma TUPLA na Lista,
        onde: CHAVE vira tupla1[0] e VALOR vira tupla1[1]

key=lambda x: x[1]  seleciona a posição do elemento das TUPLAs ou LISTAs
                    que será utilizado para fazer a ordenação, logo:
em: dados = [('jogador1', 1), ('jogador2', 4), ('jogador3', 6), ('jogador4', 3)]
    o valor contido na posição [1] de cada TUPLA dentro da lista, por exemplo,
    pode ser utilizado para ordenar a lista em ordem crescente,
    bem como o valor da posição [0] pode ser utilizado para ordenar a lista em ordem alfabética
    já que é uma string. 
"""
cont = 1
for j, v in ordenado.items():
    print(f'{cont}º lugar: {j} com {v}')
    cont += 1
print()

# guanabara
from operator import itemgetter
jogo = {'jogador1': randint(1,6), 'jogador2': randint(1,6),
        'jogador3': randint(1,6), 'jogador4': randint(1,6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou o valor {v} no dado.')
    sleep(0.4)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores:')
for k, v in enumerate(ranking):
    print(f'{k + 1}º lugar: {v[0]} com {v[1]}')
    sleep(0.4)

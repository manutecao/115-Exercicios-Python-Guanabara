jogador = dict()    # estrutura {'nome':'REBOCO', 'gols':[1, 3, 2, 0], 'total':6}
jogador['nome'] = str(input('Nome do jogador: ')).strip()
partidas = int(input('Nº de partidas jogadas: '))
golsLista = []
golsTot = 0
for p in range(0,partidas):
    golsLista.append(int(input(f'    Quantos gols na partida {p+1}? ')))
    golsTot += golsLista[p]
jogador['gols'] = golsLista[:]  # havia esquecido de fazer uma cópia usando o [:]
jogador['total'] = golsTot # also could be 'jogador['total'] = sum(golsLista)'
print('-' * 30)
print(jogador)
print('-' * 30)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('-' * 30)
print(f'O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.')
for k, v in enumerate(jogador['gols']):
    print(f'    ==> Na partida {k+1}, fez {v} gols.')
print(f'Foi um total de {jogador['total']} gols.')

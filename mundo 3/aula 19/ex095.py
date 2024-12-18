jogadores = []
jogador = dict() # estrutura {'nome':'REBOCO', 'gols':[2, 1, 3], 'total':6}
golsLista = []
esc = ' '
while esc not in 'N':
    print('-' * 20)
    jogador['nome'] = str(input('Nome do jogador: ')).strip()
    partidas = int(input('Nº de partidas jogadas: '))
    for p in range(0,partidas):
        golsLista.append(int(input(f'   Quantos gols na partida {p+1}? ')))
    jogador['gols'] = golsLista[:]
    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    jogador.clear()
    golsLista.clear()
    while True:
        esc = str(input('Cadastrar outro jogador? [S/N] ')).strip().upper()[0]
        if esc in 'NS':
            break
print('-=' * 30)
print(f'{"cod":^5}{"nome":<13}{"gols":<15}{"total":<5}')
"""print(' cod ', end='')       não funciona porque que eu apago o dicionário
for i in jogador.keys():        'jogador' depois de copiá-lo para a lista.
    print(f'{i:<13}{i:<13}{i:<15}{i:<5}')"""
print('-' * 38)
for i, v in enumerate(jogadores):
    print(f'{i:^5}{v['nome']:<13}{str(v['gols']):<15}{v['total']:<5}')
mostrar = 0
while True:
    print('-' * 38)
    mostrar = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if mostrar == 999:
        print('<< Volte sempre. >>')
        break
    elif len(jogadores) > mostrar >= 0:
        print(f'-- Levantamento do jogador {jogadores[mostrar]['nome']}:')
        for k, v in enumerate(jogadores[mostrar]['gols']):
            print(f'   No jogo {k+1}, fez {v} gols.')
    else:
        print(f'ERRO! Não existe jogador com código {mostrar}. Tente novamente.')

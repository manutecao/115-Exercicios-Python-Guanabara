# minha versão
def linha(tipo, tam):
    if tipo == 1:
        print('-' * tam)
    elif tipo == 2:
        print('-=' * tam)

def ficha(nome='', gols=-1):
    if nome == '':
        nome = '<desconhecido>'
    if gols == -1:
        gols = 0
    return f'O jogador {nome} fez {gols} gols.'

linha(1, 20)
nomeJg = str(input('Nome do jogador: ')).strip()
while True:
    numGols = input('Nº de gols: ')
    if numGols.isdigit():
        numGols = int(numGols)
        break
    elif numGols == '':
        numGols = -1
        break
    elif numGols.isalpha() or numGols.isalnum():
        print('ERRO! Digite o NÚMERO de gols.')
print(ficha(nome=nomeJg, gols=numGols))

# guamabara
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

n = str(input('Nome do jogador: ')).strip()
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gol=g)
else:
    ficha(n, g)

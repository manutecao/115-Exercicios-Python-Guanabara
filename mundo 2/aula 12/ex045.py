from random import randint
from time import sleep

# minha versao
print("""Bora jogar jokenpô.
Opções:
[1] Pedra
[2] Papel
[3] Tesoura""")
# esc = str(input('Digite sua opção (Pedra, Papel ou Tesoura): ')).lower().strip()
# print(esc)
sel = int(input('Sua opção: '))
jkp = ['pedra', 'papel', 'tesoura']
esc = jkp[sel-1]
comp = jkp[randint(0,2)]
print('Você escolheu {} e eu escolhi {}.'.format(esc, comp))
print('Processando vencedor', end=' ')
for c in range(1,3):
    print('...', end=' ')
    sleep(1)
print('...')
sleep(1)
if esc == comp:
    print('Empatou... bora dnv.')
elif (esc == 'papel') and (comp == 'pedra'):
    print(f'Jogador ganhou, Papel envolve Pedra.')
elif (esc == 'pedra') and (comp == 'tesoura'):
    print(f'Jogador ganhou, Pedra quebra Tesoura')
elif (esc == 'tesoura') and (comp == 'papel'):
    print(f'Jogador ganhou, Tesoura corta Papel')
elif (comp == 'papel') and (esc == 'pedra'):
        print(f'Computador ganhou, Papel envolve Pedra.')
elif (comp == 'pedra') and (esc == 'tesoura'):
        print(f'Computador ganhou, Pedra quebra Tesoura')
elif (comp == 'tesoura') and (esc == 'papel'):
        print(f'Computador ganhou, Tesoura corta Papel')

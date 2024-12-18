import random
from random import randint, choice

# minha versao
nomes = ['','','','']
posi = 1
for c in range(0,4):
    nomes[c] = input(f'Digite o nome do {posi}º aluno(a): ')
    posi += 1

sel = randint(0, 3)
print(f'O aluno(a) selecionado para apagar o quadro é {nomes[sel]}.')

# guanabara
n1 = input('Primeiro aluno: ')
n2 = input('Terceiro aluno: ')
n3 = input('Tereiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))

from random import shuffle

# minha versao
nomes = ['','','','']
posi = 1
for c in range(0,4):
    nomes[c] = input(f'Digite o nome do {posi}º aluno(a): ')
    posi += 1

shuffle(nomes)
posi = 1
for c in range(0,4):
    print(f'O {posi} aluno(a) a apresentar o trabalho será {nomes[c]}.')
    posi += 1

# guanabara
n1 = input('Primeiro aluno: ')
n2 = input('Terceiro aluno: ')
n3 = input('Tereiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
shuffle(nomes)
print('A ordem de apresentação do trabalho é: ')
print(nomes)

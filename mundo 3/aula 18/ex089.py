dados = []      # [['REBOCO', [9, 8], 8.5]]
while True:
    nome = str(input('Nome: ')).strip()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    dados.append([nome, [n1, n2], [(n1+n2)/2] ])
    esc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if esc == 'N':
        break
#print(dados)
print('-' * 30)
print(' Nº  | NOME     | MÉDIA')
print('-' * 25)
for num, aluno in enumerate(dados):
    print(f' {num:<6}', end='')
    print(f'{aluno[0]:<11}', end='')
    print(f'{aluno[2][0]:.2f}', end='')
    print()
print('-' * 30)
mostrar = int(input('Mostrar notas de qual aluno? (999 para parar) '))
while mostrar != 999:
    print(f'As notas de {dados[mostrar][0]} são {dados[mostrar][1][0]:.2f} e {dados[mostrar][1][1]:.2f}.')
    print('-' * 30)
    mostrar = int(input('Mostrar notas de qual aluno? (999 para parar) '))
print('-' * 30)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')

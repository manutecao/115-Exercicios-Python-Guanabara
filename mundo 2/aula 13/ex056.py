nomes = ['','','','']       # eu tenho que parar com essa mania de ficar armazenando dados que não foram pedidos
idades = [0,0,0,0]
sexo = ['','','','']        # sério
idadesc = 0
maisvelhoidade = 0
maisvelho = ''
menos20f = 0
for c in range(0,4):
    nomes[c] = str(input(f'Digite o nome da {c+1}º pessoa: '))
    idades[c] = int(input(f'Digite a idade da {c + 1}º pessoa: '))
    sexo[c] = str(input(f'Digite o sexo da {c + 1}º pessoa (M/F): ').upper())
    idadesc += idades[c]
    if idades[c] > maisvelhoidade:
        maisvelho = nomes[c]
        maisvelhoidade = idades[c]
    if sexo[c] == 'F' and idades[c] < 20:
        menos20f += 1
print(f'A média de idade do grupo é {idadesc / 4}.')
print(f'O homem mais velho é {maisvelho} com {maisvelhoidade} anos.')
print(f'Ao total, foram registradas {menos20f} mulheres com menos de 20 anos.')

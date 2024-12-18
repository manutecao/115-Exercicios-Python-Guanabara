# minha versão
"""pessoas = list()
dado = []
leves = list()
pesadas = list()
contador = 0
while True:
    dado.append(str(input('Digite o nome: ')).strip())
    dado.append(float(input('Digite o peso: ')))
    pessoas.append(dado[:])
    if dado[1] < 70:
        leves.append(dado[:])
    elif dado[1] > 100:
        pesadas.append(dado[:])
    #print(dado)
    dado.clear()
    contador += 1
    esc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if esc in 'N':
        break
#print(pessoas)
print(f'Ao total, foram cadastradas {contador} pessoas.')
print('As pessoas mais leves cadastradas foram: ',end='')
if len(leves) != 0:
    for pessoa in leves:
        print(pessoa[0], end='... ')
print()
print('As pessoas mais pesadas cadastradas foram: ',end='')
if len(pesadas) != 0:
    for pessoa in pesadas:
        print(pessoa[0], end='... ')
print()"""

# minha versão 2
"""pessoas = list()
dado = []
contador = 0
while True:
    dado.append(str(input('Digite o nome: ')).strip())
    dado.append(float(input('Digite o peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    contador += 1
    esc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if esc in 'N':
        break
print(f'Ao total, foram cadastradas {contador} pessoas.')
print('As pessoas mais leves cadastradas foram: ',end='')
for pessoa in pessoas:
    if pessoa[1] < 70:
        print(pessoa[0], end='... ')
print()
print('As pessoas mais pesadas cadastradas foram: ',end='')
for pessoa in pessoas:
    if pessoa[1] > 100:
        print(pessoa[0], end='... ')
print()"""

# minha versão 3
pessoas = list()
dado = []
contador = 0
while True:
    dado.append(str(input('Digite o nome: ')).strip())
    dado.append(float(input('Digite o peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    contador += 1       # era só usar um len()
    esc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if esc in 'N':
        break

print(f'Ao total, foram cadastradas {contador} pessoas.')
pessoas.sort(key=lambda x: x[1])    # aqui eu não fiz varredura, apenas selecionei as mais leves e as mais pesadas
if len(pessoas) < 2:
    print('')
elif len(pessoas) < 5:
    print(f'A pessoa mais LEVE é {pessoas[0][0]}')
    print(f'A pessoa mais PESADA é {pessoas[-1][0]} ')
else:
    print(f'As pessoas mais LEVES são {pessoas[0][0]} e {pessoas[1][0]}')
    print(f'As pessoas mais PESADAS são {pessoas[-1][0]} e {pessoas[-2][0]}')

# guanabara
principal = list()
temp = []
mai = men = 0
while True:
    temp.append(str(input('Digite o nome: ')).strip())
    temp.append(float(input('Digite o peso: ')))
    if len(principal) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    principal.append(dado[:])
    temp.clear()
    esc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if esc in 'N':
        break
print(f'Ao total, foram cadastradas {len(principal)} pessoas.')
print(f'O MENOR peso foi de {mai}Kg. Peso de ', end='')
for p in principal:
    if p[1] == mai:
        print(f'{p[0]} ', end='')
print()
print(f'O MENOR peso foi de {men}Kg. Peso de ', end='')
for p in principal:
    if p[1] == men:
        print(f'{p[0]} ', end='')

""" uma questão de interpretação, enquanto eu pensei que ele queria mostras as duas pessoas
dos dois pesos mais leves e mais pesados, ele quis mostrar as pessoa(s) do maior e menor peso"""

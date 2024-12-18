dados = []
temp = {}
total = soma = 0
esc = ' '
while esc not in 'N':
    temp['nome'] = str(input('Nome: ')).strip()
    while True:
        temp['sexo'] = str(input('Sexo: [F/M] ')).strip().upper()[0]
        if temp['sexo'] in 'FM':
            break
        print('Por favor, digite apenas F ou M.') # não precisa de else se ele dá 'break' caso estiver certo
    temp['idade'] = int(input('Idade: '))
    dados.append(temp.copy())
    temp.clear()
    while True:
        esc = str(input('Cadastrar outra pessoa? [S/N] ')).strip().upper()[0]
        if esc in 'NS':
            break
        print('ERRO! Digite apenas S ou N.')
print(f'- No total, {len(dados)} pessoas foram cadastradas.')
for p in dados:
    soma += p['idade']
media = soma / len(dados)
print(f'- A média das idades é de {media} anos.')
print('- As mulheres cadastradas foram: ', end='')
for p in dados:
    if p['sexo'] == 'F':
        print(p['nome'], end='')
print('\n- As pessoas com idade acima da média são:')
for p in dados:
    if p['idade'] > media:
        print()
        print(f'nome = {p['nome']}; sexo = {p['sexo']}; idade = {p['idade']};')
print('<< Saindo. >>')

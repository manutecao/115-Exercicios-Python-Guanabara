first = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão desejada: '))

# aplicando a fórmula do chat GPT
for c in range(1,11):
    print(f'{first + (c - 1) * razao}', end=' ')

print('\n')

# aplicando a explicação do guanabara, mt mais fácil
soma = first
for c in range(1,11):
    print(f'{soma}', end=' ')
    soma += razao

print('\n')

# guanabara
decimo = first + (10 - 1) * razao
for c in range(first, decimo + razao, razao):
    print(f'{c}', end=' > ')
print('Acabou')

print('\n')

for c in range(1,11):
    print(f'{first}', end=' ')
    first += razao

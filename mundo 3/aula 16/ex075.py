# minha versão
#numInt = [0, 0, 0, 0, 0]       sim, eu sei que isso não faz muito sentido, por isso fiz uma segunda versão
numInt = [0, 0, 0, 0]
#for num in range(0,5):         eram quatro não cinco números
for num in range (0,4):
    numInt[num] = int(input(f'Digite o {num+1}º valor: '))
#tupla = (numInt[0], numInt[1], numInt[2], numInt[3], numInt[4])
tupla = (numInt[0], numInt[1], numInt[2], numInt[3])
print(tupla)

print(f'O número 9 apareceu {tupla.count(9)} vezes.')
try:
    print(f'O número 3 apareceu na posição {tupla.index(3)}.')
except ValueError:
    print('O número 3 não foi digitado.')
pares = 0
for num in tupla:
    if num % 2 == 0:
        print(num, end=' ')
        pares += 1
if pares == 0:
    print('Não foram digitados números pares.')
else:
    print('foram os números pares digitados.')

# minha versão 2
#   não é porque eu estou utilizando métodos que ele ainda não ensinou que eu não sei fazer só com o que ele ensinou
#   só fico na dúvida pois ele disse para não utilizar variáveis comuns no final da explicação do exercício
#n1 = int(input('Digite o um número: '))
#n2 = int(input('Digite o outro número: '))
#n3 = int(input('Digite o mais um número: '))
#n4 = int(input('Digite o penúltimo número: '))
#n5 = int(input('Digite o último número: '))
#tupla2 = (n1, n2, n3, n4, n5)

# provável porque ele queria que fosse feito assim:
tupla2 = (int(input('Digite o um número: ')),
        int(input('Digite o outro número: ')),
        int(input('Digite o mais um número: ')),
#       int(input('Digite o penúltimo número: ')),
        int(input('Digite o último número: ')))     # eram quatro não cinco números

print(f'O número 9 apareceu {tupla2.count(9)} vezes.')

tem3 = False    # isso aqui pareceu um amargedom comparando com a do guanabara
for num in tupla2:
    if num == 3:
        tem3 = True
if tem3:
    print(f'O número 3 apareceu na posição {tupla2.index(3)}.')
else:
    print('O número 3 não foi digitado.')

pares2 = False
for num in tupla2:
    if num % 2 == 0:
        pares2 = True
if pares2:
    print('Os números pares são: ', end='')
    for num in tupla2:
        if num % 2 == 0:
            print(num, end=' ')
else:
    print('Não foram digitados números pares.')

# guanabara
tupla3 = (int(input('Digite o um número: ')),
        int(input('Digite o outro número: ')),
        int(input('Digite o mais um número: ')),
        int(input('Digite o último número: ')))
print(f'Você digitou os valores {tupla3}.')
print(f'O valor 9 pareceu {tupla3.count(9)}.')
if 3 in tupla3: # eu pensei que era possível utilizar o 'in' com números inteiros, muito menos com tuplas/listas
    print(f'O valor 3 apareceu na {tupla3.index(3) + 1}ª posição.')     # '+1' pois ele não queria a posi na tupla
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ')
for n in tupla3:
    if n % 2 == 0:
        print(n, end='')

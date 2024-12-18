# minha versão
from random import randint

numInt = [0, 0, 0, 0, 0]    # eu sabia que não era para ser feito assim, mas não consegui pensar em outra maneira
for num in range(0,5):
    numInt[num] = randint(1, 10)
tupla = (numInt[0], numInt[1], numInt[2], numInt[3], numInt[4])
print(tupla)
tuplaSorted = sorted(tupla)     # se eu crio essa variável, só preciso ordenar uma vez, no entanto, gasto mais memória
print(f'O menor é {tuplaSorted[0]}.')
print(f'O maior é {tuplaSorted[-1]}.')
print('-' * 20)
print(f'O menor é {sorted(tupla)[0]}.') # como o programa é pequeno, não faz mt diferença entre uma e outra
print(f'O maior é {sorted(tupla)[-1]}.')

print('-' * 20)
print('')

# guanabara
tuplaG = (randint(1,10), randint(1,10),
          randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados foram: ', end='')
for n in tuplaG:
    print(n, end=' ')
print(f'\nO menor é {min(tuplaG)}.')
print(f'O maior é {max(tuplaG)}.')

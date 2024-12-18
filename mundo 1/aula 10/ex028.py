from random import randint
from time import sleep

# minha versao
# acabou ficando errado pq era de 0 a 5 e eu fiz de 1 a 5. Pressa e sono...
print('Vou pensar em um número de 1 a 5.')
num = randint(1,5)
for c in range(1,6):
    print('... ', end=' ') # eu ia colocar aquela funcao que dá uma pausa no processamento por 2s, mas não lembrei qual era
print('Pronto.')
esc = int(input('Em qual número pensei? '))
if esc == num:
    print('Acertou mizeravi!')
else:
    print('Errrrrrrrooooouuuuuu!')

 # minha versao 2
print('Vou pensar em um número de 1 a 5.')
num = randint(1,5)
for c in range(1,6):
    print('... ', end=' ') # eu ia colocar aquela funcao que dá uma pausa no processamento por 2s, mas não lembrei qual era
print('Pronto.')
esc = int(input('Em qual número pensei? '))
print('Acertou mizeravi!' if esc == num else 'Errrrrrrrooooouuuuuu!')

# guanabara
pc = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5, calma lá.')
print('-=-' * 20)
player = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(2)
if pc == player:
    print('Acertou mizeravi!')
else:
    print(f'Errrrrrrrooooouuuuuu! Eu pensei no nº {pc}.')

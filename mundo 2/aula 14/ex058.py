# minha versão
from random import randint
from time import sleep
print("""Vou pensar em um número entre 0 e 10, tente adivinhar.
Pensando""", end=' ')
for c in range(0,3):
    print('...', end=' ')
    sleep(0.7)
print()
comp = randint(0,10)
tent = int(input('Sua tentativa: '))
cont = 1
while tent != comp:
    tent = int(input('Nah, tente novamente: '))
    cont += 1
print(f"""Acertou mizeravi, pensei no nº {comp} mesmo.
Você só precisou de {cont} tentativas.""")

# guanabara
computador = randint(0,10)
print("""Sou seu computador... Acabei de pensar em um número entre 0 e 10.
Será que você é capaz de adivinhar qual foi?""")
acertou = False
palpite = 0
while not acertou:  # maneira correta de fazer "while acertou != True:" ou "while acertou == False:"
    jogador = int(input('Qual é o se palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente.')
        else:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpite))

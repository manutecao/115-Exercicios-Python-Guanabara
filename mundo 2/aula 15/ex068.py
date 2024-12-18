from random import randint
from time import sleep
cont = 0
while True:
    print('{:^30}'.format('Jogo de PAR ou ÍMPAR'))
    print('-' * 30)
    #while True:
    #    playeresc = str(input('Você quer par ou ímpar? ')).strip().upper()[0]
    #    if playeresc not in 'PpIiÍí':
    #        print('Digite uma opção válida.')
    #    else:
    #        break
    playeresc = ' '
    while playeresc not in 'PIÍ':        # não precisava ser 'while True'
        playeresc = str(input('Você quer par ou ímpar? ')).strip().upper()[0]
        if playeresc not in 'PIÍ':
            print('Digite uma opção válida.')
    while True:
        try:
            playernum = int(input('Qual o número que você vai jogar? '))
        except ValueError:
            print('Você deve digitar um número inteiro.')
        else:
            if playernum < 0:
                print('Digite um número maior ou igual a 0.')
            else:
                break
    print('OK, entendi.')           #  ---------------------------  adornos  ----------------------------------
    print('Pensando em um número', end='')
    sleep(0.5)
    for c in range(1,4):
        print('... ', end='')
        sleep(0.5)
    print('')
    pc = randint(1, 10)
    print('Calculando resultado', end='')
    sleep(0.5)
    for c in range(1,4):
        print('... ', end='')
        sleep(0.5)
    print('')                                     # -----------------------------------------------------------------
                                                  # a linha abaixo é igual independente da condição
    print(f'Você jogou {playernum} e eu joguei {pc}, que somados dão {playernum + pc}, logo, o resultado é ', end='')
    if playeresc in 'P':                          # poderia também ser 'if playeresc == 'P''
        if (playernum + pc) % 2 == 0:             # eu havia repetido esse if duas vezes dentro do if superior
            print('PAR, você ganhou, PARABÉNS!!!')
            cont += 1
        else:
            print('ÍMPAR, eu ganhei.')
            break
    elif playeresc in 'IÍ':
        if (playernum + pc) % 2 != 0:           # esse teste lógico também podeia ser 'if (playernum + pc) % 2 == 1:'
            print('ÍMPAR, você ganhou, PARABÉNS!!!')
            cont +=1
        else:
            print('PAR, eu ganhei.')
            break
print('-' * 30)
if cont > 1:
    print(f'Você ganhou {cont} vezes consecutivas antes de perder. Parabéns!!!\nSaindo...')
elif cont == 1:
    print('Você ganhou uma vez e eu ganhei outra. Saindo...')
else:
    print('Saindo...')

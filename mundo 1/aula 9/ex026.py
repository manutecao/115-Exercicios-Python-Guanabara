# minha versao
frase = input('Escreva uma frase: ')
print(f'A letra "A" apareceu {frase.upper().count('A')} vezes.')
print(f'A primeira letra "A" aparece na posição: {frase.upper().find('A')}')
print(f'A última letra "A" aparece na posição: {frase.upper().rfind('A')}')

# minha versao 2
frase = str(input('Escreva uma frase: ')).strip()
print(f'A letra "A" apareceu {frase.upper().count('A')} vezes.')
print(f'A primeira letra "A" aparece na posição: {frase.upper().find('A')}')
print(f'A última letra "A" aparece na posição: {frase.upper().rfind('A')}')

""" nessa aqui o guanabara considerou melhor colocar o .upper() ja na coleta do nome para que a atribuir a variavel
    faz sentido, ja que nao sera necessario dar print nessa frase novamente, assim, economiza o .upper() nos 3 prints.
    alem disso, ele tambem considerou que a posicao do python comeca em 0 e para nos comeca em 1, colocando um + 1
    apos o .find('A'), esse e aquele tipo de coisa que tem que se pensar na interacao com o usuario. """

# guanabara
frase = str(input('Escreva uma frase: ')).strip().upper()
print(f'A letra "A" apareceu {frase.count('A')} vezes.')
print(f'A primeira letra "A" aparece na posição: {frase.find('A') + 1}')
print(f'A última letra "A" aparece na posição: {frase.rfind('A') + 1}')

from datetime import date

# minha versao
ano = int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year
idade = (atual - ano)
print(f'O atleta tem {idade} anos.', end=' ')
print('A categoria do atleta é: ', end='')
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Sênior')
else:
    print('Master')

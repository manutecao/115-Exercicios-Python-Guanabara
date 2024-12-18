from datetime import date

# minha versao
ano = int(input('Digite o ano: '))
if ((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0):
    print('Ano bissexto.')
else:
    print('Ano não bissexto.')

# guanabara
# minha versao
ano = int(input('Digite o ano: ( 0 para o ano atual ) '))
if ano == 0:
    ano = date.today().year
if ((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0):
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não bissexto.')

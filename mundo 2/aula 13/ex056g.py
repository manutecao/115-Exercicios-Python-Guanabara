nome = ''
idade = 0
sexo = ''
media = 0
menos20f = 0
maisvelhoidade = 0
maisvelho = ''
for c in range(0,4):
    nome = str(input(f'Digite o nome da {c+1}º pessoa: '))
    idade = int(input(f'Digite a idade da {c + 1}º pessoa: '))
    sexo = str(input(f'Digite o sexo da {c + 1}º pessoa (M/F): ').strip().upper())
    media += idade
    # if idade > maisvelhoidade:        eu me esqueci de que ele quer saber apenas o HOMEM mais velho
# if (sexo == 'M') and (sexo in 'Mm'):  prefere procurar M min. ou mai. na estring 'Mm' do que usar .upper() ou .lower()
    if c == 1 and sexo in 'Mm':
        maisvelhoidade = idade      # Guanabara Redundâncias LTDA.
        maisvelho = nome
    if (sexo == 'M') and (idade > maisvelhoidade):
        maisvelhoidade = idade
        maisvelho = nome
# if (sexo in 'Ff') and idade < 20:  prefere procurar F min. ou mai. dentro de 'Ff' do que usar o .upper() ou .lower()
    if sexo == 'F' and idade < 20:
        menos20f += 1
print(f'A média de idade do grupo é {media / 4}.')
print(f'O homem mais velho é {maisvelho} com {maisvelhoidade} anos.')
print(f'Ao total, foram registradas {menos20f} mulheres com menos de 20 anos.')

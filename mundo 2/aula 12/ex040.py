n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1 + n2) / 2
print(f'A média entre as notas {n1} e {n2} é {m:.2f}.')

# minha versao
# if m < 5.0:
#    print('Reprovado.')
# elif (m >= 5.0) and (m <= 6.9):                          # mesma coisa que colocar m < 7
#    print('Recuperação.')
# elif m > 7.0:                                         # e se o cara tirar exatamente 7?
#    print('Aprovado.')

if 7 > m >= 5:
    print('Recuperação,.')
elif m < 5:
    print('Reprovado.')
elif m >= 7:
    print('Aprovado.')

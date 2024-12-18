print('-' * 20)
print('Cadastro de pessoas')
print('-' * 20)
homens = mais18 = mulhermenos20 = c = 0
while True:
    while True:
        try:
            idade = int(input(f'Digite a idade da {c + 1}ª pessoa: '))
        except ValueError:
            print('Digite um número inteiro.')
        else:
            if idade < 0:
                print('A idade deve ser pelo menos 0.')
            else:
                break

    #while True:
    sexo = ' '
    while sexo not in 'FM':
            sexo = str(input(f'Digite o sexo da {c + 1}ª pessoa: [M/F] ')).strip().upper()[0]
            if sexo not in 'FM':
                print('Digite uma opção válida: (F ou M)')
    #       else:
    #           break

    c += 1
    if idade > 18:
        mais18 += 1
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        mulhermenos20 += 1

    #while True:
    esc = ' '
    while esc not in 'SN':
        esc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if esc not in 'SN':
            print('Digite uma opção válida: (S ou N)')
    #   else:
    #       break
    if esc in 'N':      # também pode ser 'if esc == 'N':'
        break

print(f"""\nAo todo foram lidas {c} pessoas, sendo:
{mais18} maiores de 18 anos,
{homens} homens,
e {mulhermenos20} mulheres abaixo dos 20 anos.""")

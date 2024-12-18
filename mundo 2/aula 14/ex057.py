# minha versao
sexo = ' '
while not(sexo in 'FfMm'):
    sexo = str(input('Digite o sexo da pessoa [F/M]: '))
    if not(sexo in 'FfMm'):
        print('Digite uma opção válida.')
print(f'A entrada {sexo} é valida.')

# guanabara
# lembrar de sempre dar .strip() nas entradas manuais
# aqui ele já colocou a resposta em maiusculo atém de pegar apenas a primeira caractere
sexo = str(input('Digite o sexo da pessoa [F/M]: ')).strip().upper()[0]
while sexo not in 'FfMm': # maneira certa de fazer o "not(sexo in 'FfMm')", mas eu acho que a str poderia ser só 'FM'
    sexo = str(input('Dados inválidos. Por favor, digite seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} foi registrado com sucesso.'.format(sexo))

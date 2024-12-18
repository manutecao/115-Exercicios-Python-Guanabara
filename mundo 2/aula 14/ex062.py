# minha versão

termos = 10
first = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
while termos != 0:
    cont = 1
    while cont < termos + 1:
        print(f'{first} -> ', end=' ')
        first = first + razao
        cont += 1
    print('PAUSA')
    termos = int(input('Quantos termos mais quer mostrar? ( 0 para sair ) '))
print('Saindo aqui, tchau.')

# guanabara
print('{:^20}'.format('Gerador de PA'))
print('-' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar: '))
print('Progressão finalizada com {} termos mostrados.'.format(total))

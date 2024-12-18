# minha versão
first = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1
while cont < 11:
    #first = first + razao          se colocar a soma antes ele mostra p 2º termo até o 11º
    print(first, end=' -> ')
    first = first + razao
    cont += 1
print('FIM')

# guanabara
print('{:^20}'.format('Gerador de PA'))
print('-' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
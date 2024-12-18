# minha versão
tabela = ('Botafogo', 'Palmeiras', 'Internacional', 'Fortaleza', 'Flamengo',
          'São Paulo', 'Cruzeiro', 'Bahia', 'Corinthians', 'Atlético-MG',
          'Vasco da Gama', 'EC Vitória', 'Juventude', 'Athlético-PR', 'Grêmio',
          'Fluminense', 'Criciúma', 'Bragantino', 'Cuiabá', 'Atlético-GO')

print('Os cinco primeiros colocados são:')
for posi, time in enumerate(tabela[0:5]):
    print(f'{posi + 1}º lugar - {time}')
print('-' * 30)

print('Os últimos quatro colocados são:')
for time in tabela[16:21]:
    print(f'{(tabela.index(time)) + 1}º lugar - {time}')
print('-' * 30)
# era esse 'tabela[-4:]' que eu estava tentando fazer antes, o '-1' no segundo parâmetro sempre é ignorado
# quando se quer que ele vá até o final, basta deixá-lo vazio
for time in tabela[-4:]:
    print(f'{(tabela.index(time)) + 1}º lugar - {time}')
print('-' * 30)

print('Os times do Brasileirão 2024 em ordem alfabética são:')
tabela_sorted = sorted(tabela)
for time in tabela_sorted:
    print(time, end=', ')
print('')
print('-' * 30)

# em 2024 a Chapecoense não está na série A do Brasileirão, portanto, escolhi o Corinthians para prosseguir
print(f'O Corinthians está na {(tabela.index('Corinthians')) + 1}ª posição.')

# guanabara
times = ('Botafogo', 'Palmeiras', 'Internacional', 'Fortaleza', 'Flamengo',
          'São Paulo', 'Cruzeiro', 'Bahia', 'Corinthians', 'Atlético-MG',
          'Vasco da Gama', 'EC Vitória', 'Juventude', 'Athlético-PR', 'Grêmio',
          'Fluminense', 'Criciúma', 'Bragantino', 'Cuiabá', 'Atlético-GO')

print('-=' * 15)
print('Lista de times do Brasileirão 2024:')
print(times)
print('-=' * 15)
print('Lista dos cinco primeiros times da tabela:')
print(times[0:5])
print('-=' * 15)
print('Os quatro últimos times da tabela são:')
print(times[-4:])
print('-=' * 15)
print('Times em ordem alfabética:')
print(sorted(times))
print('-=' * 15)
print(f'O Corinthians está na {(times.index('Corinthians')) + 1}ª posição.')

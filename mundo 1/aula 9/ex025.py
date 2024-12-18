# minha versao
nome = input('Digite o nome completo: ')
tem = nome.strip().upper().find('SILVA')
if tem == -1:
    print('Este nome não tem "SILVA".')
else:
    print(f'Este nome tem "Silva" na posição {tem}.')

# minha versao 2
nome = str(input('Digite o nome completo: ')).strip()
print(f'O nome tem "Silva"? {nome.upper().find('SILVA') >= 0}')

""" preciso comecar a pensar em maneiras mais simples para resolver problemas
    estou muito preso as estruturas que aprendi e nao dando atencao as funcoes e metodos da linguagem
    extatamente o que faz ela ser poderosa como e. """

# guanabara
nome = str(input('Digite o nome completo: ')).strip()
print(f'O nome tem "Silva"? {'silva' in nome.lower()}')
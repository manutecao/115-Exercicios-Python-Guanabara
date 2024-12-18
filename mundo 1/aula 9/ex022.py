# minha versao
nome = input('Insira o seu nome completo: ') # ERRADO pois não usei o .strip() nem forcei a declaracao com str()
print(f'O nome todo em maiúsculo: {nome.upper()}')
print(f'O nome todo em minúsculo: {nome.lower()}')
print(f'O nome completo sem espaços tem {len(nome.strip())} letras') # ERRADO pois conta os espaços entre os nomes
print(f'Apenas o nome {nome.split()[0]} tem {len(nome.split()[0])} letras.')

# guanabara
nome = str(input('Insira o seu nome completo: ')).strip()
print(f'O nome todo em maiúsculo: {nome.upper()}')
print(f'O nome todo em minúsculo: {nome.lower()}')
print(f'O nome completo tem {len(nome) - nome.count(' ')} letras')
#print(f'Seu primeiro nome tem {nome.find(' ')} letras.')
#ou
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras.'.format(separa[0],len(separa[0])))

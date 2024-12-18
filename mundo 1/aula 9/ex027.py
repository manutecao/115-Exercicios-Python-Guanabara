# minha versao
nome = input('Digite o nome completo: ')
lista = nome.split()
print(f'O primeiro nome é {lista[0]},\n e o último é {lista[-1]}.')

# minha versao 2
nome = str(input('Digite o nome completo: ')).strip().split()
print(f'O primeiro nome é {nome[0]},\n e o último é {nome[-1]}.')

""" eu pensei que o lista[len(lista)] nao funcionava, mas e porque esqueci que o len() retorna a quantidade de caracteres
    de uma string comecando por 1, e as posicoes da string comecam por 0. foi so colocar o -1 na frente que funcionou.
    ainda assim acho mais facil so usar o -1 mesmo, e mais pratico. """

# guanabara
nome = str(input('Digite o nome completo: '))
lista = nome.split()
print(f'O primeiro nome é {lista[0]},\n e o último é {lista[len(lista)-1]}.')
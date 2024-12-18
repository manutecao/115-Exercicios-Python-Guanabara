# minha versao
n = int(input('Digite um número inteiro: '))
print(f'Sobre o número {n}, seu dobro é {n * 2}, seu triplo é {n * 3} e sua raiz é {n ** (1/2)}')

# guanabara 1
n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print('Sobre o número {}, \nseu dobro é {}, \nseu triplo é {} \ne sua raiz é {:.2f}'.format(n, dobro, triplo, raiz))

# guanabara 2
n = int(input('Digite um número: '))
print('Sobre o número {}, \nseu dobro é {}, \nseu triplo é {} \ne sua raiz é {:.2f}'.format(n, n*2, n*3, pow(n,(1/2))))
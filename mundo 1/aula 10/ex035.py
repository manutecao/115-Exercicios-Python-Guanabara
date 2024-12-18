# minha versao
n1 = input('1º reta: ')
n2 = input('2º reta: ')
n3 = input('3º reta: ')
if n1 + n2 > n3 and n2 + n3 > n1 and n1 + n3 > n2:
    print('Sim, dá para formar um triângulo.')
else:
    print('Rola não pae.')

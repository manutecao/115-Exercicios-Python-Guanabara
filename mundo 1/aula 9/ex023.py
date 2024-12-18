# miha versao
num = str(input('Digite um número inteiro de 0 a 9999: '))
tam = len(num)
print(tam)
print(f'Unidade: {num[tam-1:tam]}')     # saiu errado
print(f'Dezena: {num[tam-2:tam-1]}')
print(f'Centena: {num[tam-3:tam-2]}')
print(f'Milhar: {num[tam-4:tam-3:]}')   # esse aqui retorna a posicao 0 quando a entrada é dezena, soma de sinais?

# guanabara
num = int(input('Digite um número inteiro de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

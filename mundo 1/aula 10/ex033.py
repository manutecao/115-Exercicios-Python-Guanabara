# minha versao ( eu sei que maneiras maelhores de fazer isso, mas eu estou tentando fazer apenas com o que ele ensinou)
n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
n3 = int(input('3º número: '))
maior = 0 # nao era necessario declarar essas vaziáveis antes
menor = 0
if n1 > n2 and n1 > n3:
    maior = n1
else:
    if n2 > n3:
        maior = n2
    else:
        maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
else:
    if n2 < n3:
        menor = n2
    else:
        menor = n3
print(f'O maior número é {maior} e o menor é {menor}.')

# guanabara
a = int(input('1º número: '))
b = int(input('2º número: '))
c = int(input('3º número: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior número é {maior} e o menor é {menor}.')

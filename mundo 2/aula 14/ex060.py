num = int(input('Digite um número: '))
prod = num
print(f'{num}! =', end=' ')
while num > 0:
    if num == 1:
        print(f'{num}', end=' = ')
        num -= 1
    else:
        print(f'{num}', end=' + ')
        prod = prod * (num -1)
        num -= 1
print(f'{prod}')

# guanabara
from math import  factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))

# guanabara
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando fatorial de {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c  # mesmo que " f = f * c "
    c -= 1
print('{}'.format(f))

# desafio extra
num = int(input('Digite um número para calcular o fatorial: '))
prod = 1
print(f'Fatorial de {num}! = ', end='')
for c in range(num, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    prod *= c
print(prod)

# minha versão
n = int(input('Digite quantas posições da sequência de Fibonacci quer ver: '))
c = 0
frs = 0
sec = 1
new = 1
while c < n:
    if c == 0:
        print(frs, end=' - ')
        c += 1
    elif c == 1:
        print(sec, end=' - ')
        c += 1
    elif c == n-1:
        new = frs + sec
        print(new)
        frs = sec
        sec = new
        c += 1
    else:
        new = frs + sec
        print(new, end=' - ')
        frs = sec
        sec = new
        c += 1

# guanabara
print('-' * 30)
print('{:^30}'.format('Sequência de Fibonacci'))
print('-' * 30)
n - int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('-' * 30)

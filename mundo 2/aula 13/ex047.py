# versao correta
for c in range(2,51,2):
    print(c, end=' ')

print('')

# daqui pra baixo é descartável

for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')

print('')

for c in range(0,51,2):
    if c == 0:
        print('')
    else:
        print(c,end=' ')

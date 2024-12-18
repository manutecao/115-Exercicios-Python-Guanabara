from math import copysign
n = 0
while True:
    n = int(input('Deseja ver a tabuada de qual valor? '))
    if n < 0:
       break
    #if copysign(1, n) == -1:    # vi na internet, não me parece eficiente para este caso
    #    print(copysign(1, n)       # só para ver se a saída está certa
    #    break
    print('-' * 30)
    for c in range(1,11):
        print(f'{n} x {c:2} = {n * c}')
    print('-' * 30)
print('Fim do programa de tabuada.')

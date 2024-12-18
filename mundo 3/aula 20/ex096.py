def area(a, b):
    print(f'A área de um terreno {a} x {b} é {a * b}m².')

print(f'{'Controle de Terrenos':25}')
print('-' * 25)
l = float(input('Largura: (m) '))
c = float(input('Comprimento: (m) '))
area(l, c)
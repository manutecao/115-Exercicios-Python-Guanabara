# minha versão
n = s = c = 0
while n != 999:         # eu deveria ter usado o while True aqui
    n = int(input('Digite um número inteiro: (999 para parar) '))
    if n == 999:
        break
    s += n
    c += 1
print(f'O total dos {c} números digitados é {s}.')

# guanabara
soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'O total dos {cont} valores digitados é {soma}.')

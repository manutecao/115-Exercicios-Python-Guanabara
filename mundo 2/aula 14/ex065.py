# minha versão
cont = soma = num = maior = 0
menor = 9999999999999999
esc = ''
while esc.upper() != 'N':
    num = int(input(f'Digite o {cont + 1}º número inteiro: '))
    soma += num
    cont += 1
    if num < menor:
        menor = num
    if num > maior:
        maior = num
    esc = str(input('Deseja continuar? [S/N]: '))
print(f"""Ao todo foram digitados {cont} números,
a MÉDIA deles é {soma/cont},
enquanto o MENOR é {menor} e o MAIOR é {maior}.""")

# guanabara
resp = 'S'
soma = media = quant = maior = menor = 0
while resp in 'S':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if cont == 1:
        maior = menor = num     # melhor do que a gambiarra de declarar " menor = 999999999999999999 "
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {]'.format(quant, media))
print('O MAIOR valor foi {} e o MENOR foi {}.'.format(maior, menor))

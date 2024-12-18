# minha versão
cont = soma = num = 0
while num != 999:
    num = int(input('Digite quantos números inteiros quiser somar (ou 999 para sair): '))
    if num != 999:
        soma += num
        cont += 1
print(f"""Ao todo foram digitados {cont} números,
e a soma de todos eles é {soma}.""")

# guanabara
cont = soma = num = 0
num = int(input('Digite quantos números inteiros quiser somar (ou 999 para sair): '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite quantos números inteiros quiser somar (ou 999 para sair): '))
print(f"""Ao todo foram digitados {cont} números,
e a soma de todos eles é {soma}.""")

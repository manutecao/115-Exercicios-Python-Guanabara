soma = 0
for c in range(1,7):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        soma += num
print(f'Dos seis número coletados, a soma dos pares é {soma}.')

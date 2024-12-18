# minha versão
rs50 = rs20 = rs10 = rs1 = 0
valor = int(input('Qual o valor que deseja sacar? R$ '))
saque = valor
while valor >= 50:
    rs50 += 1
    valor -= 50
while valor >= 20:
    rs20 += 1
    valor -= 20
while valor >= 10:
    rs10 += 1
    valor -= 10
while valor > 0:
    rs1 += 1
    valor -= 1
print(f'Ao sacar o valor de {saque}, você receberá:')
if rs50 > 0:
    print(f'{rs50} cédulas de R$ 50.00')
if rs20 > 0:
    print(f'{rs20} cédulas de R$ 20.00')
if rs10 > 0:
    print(f'{rs10} cédulas de R$ 10.00')
if rs1 > 0:
    print(f'{rs1} cédulas de R$ 1.00')

# guanabara
valor = int(input('Qual o valor que deseja sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:     # nesse momento eu tinha até esquecido que estava praticando o 'while True'
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} de R$ {ced:.2f}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

# alternativa à versão guanabara
valor = int(input('Qual o valor que deseja sacar? R$ '))
total = valor
ced = 50
totced = 0
while total >= 0:     # também funciona fazer assim
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} de R$ {ced:.2f}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
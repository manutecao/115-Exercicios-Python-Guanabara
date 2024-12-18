# minha versao
conta = float(input('Digite quanto você tem na carteira: '))
print(f'Seus R$ {conta} Reais equivalem a $ {conta / 3.27:.2f} dólares.')

# versao guanabara
real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dollar = real / 3.27
print('Com R$ {} você consegue comprar U$${:.2f}.'.format(real, dollar))
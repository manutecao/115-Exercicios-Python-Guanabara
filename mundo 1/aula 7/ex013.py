# minha versao
sal = float(input('Digite o salário atual do funcionário: '))
print(f'O salário do funcionário com 15% de aumenta passa a ser de R$ {sal * 1.15} Reais.')

# guanabara
sal = float(input('Digite o salário atual do funcionário: R$ '))
novo = sal + (sal*15/100)
print('O salário de R${:.2f} com 15% de aumento passa a ser de {:.2f}.'.format(sal, novo))

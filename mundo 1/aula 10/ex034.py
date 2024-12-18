# minha versao
sal = float(input('Digite o salário: '))
if sal > 1200:
    print(f'Com 10% de aumento este salário passará a ser de R$ {sal+(sal/10*100)}.')
else:
    print(f'Com 15% de aumento este salário passará a ser de R$ {sal+(sal/15*100)}.')

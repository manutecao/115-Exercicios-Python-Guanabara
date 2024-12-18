# minha versao
casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salário? '))
tempo = int(input('Em quantos anos você pretende pagar a casa? '))
sal30 = sal*30/100
prest = casa / (tempo * 12)
print('Nessas condições, a prestação seria de R$ {:.2f} enquanto seu teto seria R$ {:.2f}.'.format(prest, sal30))
if prest > sal30:
    print('Seu empréstimo foi negado.')
else:
    print('Seu empréstimo foi aprovado.')

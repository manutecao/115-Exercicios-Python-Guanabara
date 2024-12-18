# minha versao
preco = float(input('Digite o preço do produto: '))
print("""Qual é a forma de pagamento?
[1] à vista ( 10% desc. )
[2] à vista no cartão ( 5% desc. )
[3] até 2x no cartão
[4] 3x ou mais no cartão ( 20% juros )""")
esc = int(input('Sua opção: '))
if esc == 1:
    print('O valor à vista é R$ {:.2f}.'.format(preco - (preco*10/100)))
elif esc == 2:
    print('O valor à vista no cartão é R$ {:.2f}.'.format(preco - (preco * 5 / 100)))
elif esc == 3:
    print('Sua compra de R$ {:.2f} sairá em 2x de R$ {:.2f} no cartão.'.format(preco, preco / 2))
elif esc == 4:
    parcelas = int(input('Qual em quantas parcelas quer dividir? '))
    total = preco + (preco * 20 /100)
    print('Sua compra de R$ {:.2f} sairá por {:.2f} em {} x de R$ {:.2f} no cartão..'.format(preco, total, parcelas, total / parcelas))
else:
    print('\033[31mDigite uma opção válida.\033[m')

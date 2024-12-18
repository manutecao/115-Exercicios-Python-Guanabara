# minha versao

preco = float(input('Digite o preço do produto: '))
print(f'O preço do produto com 5% de desconto é R$ {preco - (preco * 0.05)} Reais.')

# guanabara
preco = float(input('Digite o preço do produto: '))
novo = preco - (preco*5/100)
print('O produto que custa R${:.2f} com 5% de desconto passa a ser R${:.2f}.'.format(preco, novo))

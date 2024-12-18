# minha vesao 1 e 2
dist = float(input('Distanca a ser percorrida em KM: '))
if dist <= 200:
    print('Você vai pagar R$ {:.2f} nessa viagem.'.format(dist * 0.5))
else:
    print('Você vai pagar R$ {:.2f} nessa viagem.'.format(dist * 0.45))
# ou
print('O preço da sua passagem é: ')
print('R$' + str(dist * 0.5) if dist < 200 else 'R$' + str(dist * 0.45))

# guanabara 2
dist = float(input('Distanca a ser percorrida em KM: '))
preco = dist * 0.5 if dist < 200 else dist * 0.45
print('O preço da sua passagem é R$ {:.2f}.'.format(preco))
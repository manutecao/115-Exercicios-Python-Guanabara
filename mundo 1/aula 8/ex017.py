from math import hypot, sqrt

# minha versao
opo = float(input('Digite o cateto oposto: '))
adj = float(input('Digite o cateto adjacente: '))
print('Um triangulo com o cateto oposto de {} e adjacente de {} tem a hipotenusa de {:.2f}.'.format(opo, adj, hypot(opo, adj)))

# guanabara
opo = float(input('Digite o cateto oposto: '))
adj = float(input('Digite o cateto adjacente: '))
hi = (opo ** 2 + adj ** 2) ** (1/2)
print('Um triangulo com o cateto oposto de {} e adjacente de {} tem a hipotenusa de {:.2f}.'.format(opo, adj, hi))

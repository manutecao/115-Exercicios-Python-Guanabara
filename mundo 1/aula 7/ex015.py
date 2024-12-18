# minha versao
dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilometros foram percorridos? '))
custo_dia = dias * 60
custo_km = km * 0.15
custo_total = custo_dia + custo_km
print('O custo do aluguel do veículo que foi alugado por {} dias e rodou {:.2f} KMs é de R$ {}.'.format(dias, km, custo_total))

# guanabara
dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilometros foram percorridos? '))
custo = (dias * 60) + (km * 0.15)
"""
// poderia fazer esse cálculo sem as aspas pois para essa equação a ordem de precedencia e perfeita
// custo = dias * 60 + km * 0.15
"""
print('O custo do aluguel do veículo que foi alugado por {} dias e rodou {:.2f} KMs é de R$ {}.'.format(dias, km, custo))

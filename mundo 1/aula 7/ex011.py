# minha versao
lar = float(input('Digite a LARGURA da parede em metros: '))
alt = float(input('Digite a ALTURA da parede em metros: '))
area = lar * alt
print(f'A área da parede é: {area:.2f}m².')
print(f'Serão necessários {area / 2:.2f} litros de tinta para pintar essa parede.')

# guanabara
lar = float(input('Digite a LARGURA da parede em metros: '))
alt = float(input('Digite a ALTURA da parede em metros: '))
area = lar * alt
tinta = area / 2
print('A área da parede é: {:.2f}m².'.format(area))
print('Serão necessários {:.1f}l de tinta para pintar essa parede.'.format(tinta))

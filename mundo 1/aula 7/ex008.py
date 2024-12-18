# minha versao

num = float(input('Digite um valor em metros: '))
print(f'{num} metros é igual a {num * 100:.0f} centímetros e {num * 1000:.0f} milímetros.')

# minha versao 2
n = float(input('Digite uma distancia em metros: '))
print('A medida {} corresponde a:\n{:.3f} km\n{:.2f} hm\n{:.1f} dam\n{:.0f} cm\n{:.0f} mm'.format(n, n/1000, n/100, n/10, n*10, n*1000))

# guanabara
n = float(input('Digite uma distancia em metros: '))
km = n / 1000
hm = n / 100
dam = n / 10
cm = n * 100
mm = n * 1000
print('A medida {}m corresponde a:'.format(n))
print('{:.3f}km\n{:.2f}hm\n{:.1f}dam\n{:.0f}cm\n{:.0f}mm'.format(km, hm, dam, cm, mm))

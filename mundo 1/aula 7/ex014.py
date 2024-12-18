# minha versao
temp = float(input('Informe a temperatura em ºC: '))
print(f'A temperatura de {temp}º Celsius em Farenheit é {temp * 1.8 + 32}º.')

# guanabara
c = float(input('Informe a temperatura em ºC: '))
f = ((9 * c) / 5) + 32
"""
//ou
f = 9 * c /5 + 32
// pois a ordem de precedencia funcionaria perfeitamente nessa equacao
// OBS: tambem funcionaria na MINHA VERSAO: temp * 1.8 + 32
"""
print('A temperatura de {:.2f}º Celsius em Farenheit é {:.2f}º.'.format(c,f))

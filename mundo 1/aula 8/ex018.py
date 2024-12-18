from math import radians, sin, cos, tan

# minha versao
ang = int(input('Digite um ângulo inteiro em graus: '))
seno = sin(radians(ang))
coss = cos(radians(ang))
tan = tan(radians(ang))
print('O ângulo de {}º tem o seno {:.2f} e cosseno {:.2f}, com a tengente de {:.2f}.'.format(ang, seno, coss, tan))

frase = str(input('Digite uma frase: ')).strip().lower().replace(' ', '')
                                                        # print(frase)
tam = len(frase)
                                                        # print(tam)
cont = 0
                                                        # end = int(tam // 2)
                                                        # for c in range(0, tam - 1):
                                                        # (1) faz a verificação em ambos os sentidos, logo, desnecessario
for c in range(0, int(tam // 2)):   # , end)
    if frase[c] == frase[tam - 1 - c]:
        cont += 1
                                                        # print(cont)
                                                        # if cont == (tam - 1):         # (1) ...
if cont == int(tam // 2):   # == end
    print('SIM, essa frase é palíndromo.')
else:
    print('NÃO, essa frase NÃO é palíndromo.')

# guanabara
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()                                # era só dar .replace() ...
                                                        # print(palavras)
junto = ''.join(palavras)
                                                        # print(junto)
inverso = ''
for letra in range(len(junto) -1, -1, -1):              # genial, era só inverter a frase e comparar com a original
                                                        # print(junto[letra], end='')
    inverso += junto[letra]
                                                        # print(junto)
                                                        # print(inverso)
if inverso == junto:
    print('SIM, essa frase é palíndromo.')
else:
    print('NÃO, essa frase NÃO é palíndromo.')

# guanabara 2
inverso = junto[::-1]               # na moral kkkkk, eu demorei mo tempão pra fazer o meu ...
                                                        # print(junto)
                                                        # print(inverso)
if inverso == junto:
    print('SIM, essa frase é palíndromo.')
else:
    print('NÃO, essa frase NÃO é palíndromo.')

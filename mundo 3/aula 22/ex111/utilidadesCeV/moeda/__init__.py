def aumentar(valor, por=0, formatado=False):
    if formatado:
        return moeda(valor + (valor * por / 100))       # minha versão
    else:
        return valor + (valor * por / 100)

def diminuir(valor, por=0, formatado=False):
    resultado = valor - (valor * por / 100)
    if formatado:                                        # minha versão 2
        return moeda(resultado)
    else:
        return resultado

def dobro(n=0, formatado=False):
    resultado = n * 2
    return moeda(resultado) if formatado else resultado # minha versão 3

def metade(n, formatado=False):
    resultado = n / 2
    return resultado if formatado is False else moeda(resultado) # guanabara

def moeda(valor, currency='R$'):
    return currency + ' ' + str(f'{valor:.2f}').replace('.',',')

def resumo(valor=0, aumento=10, reducao=5):
    print('-' * 30)
    print(f'{'RESUMO DO VALOR':^30}')
    print('-' * 30)
    tabela = dict()
    tabela['Preço analisado:'] = moeda(valor)
    tabela['Dobro do preço:'] = dobro(valor,True)
    tabela['Metade do preço:'] = metade(valor, True)
    tabela[f'{aumento}% de aumento:'] = aumentar(valor, aumento, True)
    tabela[f'{reducao}% de redução:'] = diminuir(valor, reducao, True)
    for k, v in tabela.items():
        print(f'{k:<19}{v:<6}')
    print('-' * 30)

# guanabara
def resumo2(valor=0, aumento=10, reducao=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor,True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(valor, reducao, True)}')
    print('-' * 30)
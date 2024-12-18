def linha(tipo, tam):
    if tipo == 1:
        print('-' * tam)
    elif tipo == 2:
        print('-=' * tam)

def vota(nasc):
    from datetime import datetime
    esseano = datetime.today().year
    idade = esseano - nasc
    if idade < 16:
        situacao = 'NEGADO'
    elif idade > 65 or idade < 18:
        situacao = 'OPCIONAL'
    else:
        situacao = 'OBRIGATÓRIO'
    return f'Com {idade} anos, o voto é {situacao}.'

linha(1, 15)
anoNasc = int(input('Em que ano você nasceu? '))
print(vota(anoNasc))

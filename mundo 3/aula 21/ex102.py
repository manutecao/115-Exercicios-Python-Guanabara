# minha versão
def linha(tipo, tam):
    if tipo == 1:
        print('-' * tam)
    elif tipo == 2:
        print('-=' * tam)

def fatorial(num, mostrar=False):
    """
    --> Calcula o FATORIAL de um número:
    :param num: o número da qual o fatorial será calculado
    :param mostrar: (opiconal)
        True = retorna a expressão completa 'str', ex: 5 x 4 x 3 x 2 x 1 = 120
        False = retorna o resuldado da expressão 'int', ex: 120
    :return: depende da opção 'mostrar', que é 'False' por padrão.
    """
    if not mostrar:
        acc = 1
        for n in range(num, 0, -1):
            acc *= n
        return acc
    else:
        acc = 1
        frase = ''
        for n in range(num, 0, -1):
            acc *= n
            if n == 1:
                frase += str(n) + ' = '
            else:
                frase += str(n) + ' x '
        frase += str(acc)
        return frase

linha(1,25)
print(fatorial(5))
#help(fatorial)

""" a minha ficou errada pois minha função retorna o fatorial ou sua expressão,
a do guanabara sempre retorna o fatorial, mas com a opção de mostrá-lo na tela."""

# guanabara
def fatorial(num, show=False):
    """ DocString
    --> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a expressão fatorial na tela.
    :return: O valor fatorial de 'num'.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(fatorial(5, show=True))
help(fatorial)
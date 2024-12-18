#expressao = str(input('Digite a expressão: ')).strip()
expressao = 'a+((b+c)-(d+e)*f)'
if expressao.count('(') != expressao.count(')'): #verifica se a qtd de abre e fecha parênteses é o mesmo
    print('Sua expressão não é válida.')
else:
    lista = []
    valido = True
    for item in expressao:
        if item == '(':
            lista.append(item)  # coloca o '(' disponível para ser fechado
        elif item == ')':
            if len(lista) > 0:  # verifica se tem pelo menos '(' para este ')' feche
                lista.pop()
            else:
                valido = False  # determina a expressão como inválida
                break   # interrompe o laço de repetição assim que houver um fecha parêntese sem abertura
    if valido:
        print('Sua expressão é válida.')
    else:
        print('Sua expressão não é válida')

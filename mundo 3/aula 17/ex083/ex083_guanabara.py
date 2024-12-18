expr = str(input('Digit a expressão: ')).strip()
pilha = []
for item in expr:
    if item == '(':
        pilha.append('(')
    elif item == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')') # é assim que ele registra o erro, lidando com a paridade e a ordem ao mesmo tempo
            break
if len(pilha) == 0:
    print('Sua expressão é válida.')
else:
    print('Sua expressão está errada.')

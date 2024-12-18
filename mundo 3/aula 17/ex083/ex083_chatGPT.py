exp = str(input('Digite a expressão: ')).strip()
#exp = 'a+((b+c)-(d+e)*f)'
# Verifica se a expressão tem o mesmo número de '(' e ')'
if exp.count('(') != exp.count(')'):
    print('Sua expressão não é válida.')
else:
    pilha = []
    valido = True

    # Percorre cada caractere da expressão
    for char in exp:
        if char == '(':
            pilha.append(char)  # Empilha parênteses de abertura
        elif char == ')':
            if len(pilha) > 0:
                pilha.pop()  # Remove o último parêntese de abertura correspondente
            else:
                valido = False  # Parêntese de fechamento sem correspondente
                break
    print(exp)

    # Verifica se a pilha está vazia no final
    if valido and len(pilha) == 0:
        print('Sua expressão é válida.')
    else:
        print('Sua expressão não é válida.')

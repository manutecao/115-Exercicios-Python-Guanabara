# não funcionou 100%, mas eu tentei o que pude sem pesquisar como fazer exatamente o que o enunciado pede

#exp = str(input('Digite a expressão: ')).strip()
exp = ')a+b(' #a+((b+c)-(d+e)*f)'
abrindo = exp.count('(')
fechando = exp.count(')')
cont = 0
if abrindo == fechando:
    while True:
        if '(' in exp:
            last = exp.rindex('(')
        else:
            break
        #print(last)
        c = last + 1
        #print(c)
        fecha = False
        while c < len(exp):
            fecha = False
            if exp[c] == ')':
                fecha = True
                #print('ok')
                cont += 1
                exp = exp[:c] + exp[c + 1:]
                exp = exp[:last] + exp[last + 1:]
                break
            c += 1
            #print(c)
        if not fecha:
            break
        #print(exp)
        if cont == abrindo:
            print('Sua expressão é válida.')
else:
    print('Sua expressão não é válida.')

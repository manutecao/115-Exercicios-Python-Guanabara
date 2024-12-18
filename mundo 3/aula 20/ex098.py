from time import sleep

def linha(tipo, tam):
    if tipo == 1:
        print('-' * tam)
    elif tipo == 2:
        print('-=' * tam)

def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}:')
    if p == 0:
        p = 1
        print('(Não há como prosseguir com Passo 0,\nentão farei com Passo 1.)')
    if f > i:
        if p < 0:
            print('(Não é possível contar em ordem crescente com passo negativo,\nvou considerar positivo.)')
            p = p * -1
        f += 1
    elif i > f:
        f -= 1
        if p > 0:   # eu esperava que a entrada do passo sempre seria negativa
            p = -p  # quando a contagem fosse em ordem decrescente
    sleep(0.3)
    for c in range(i, f, p):
        print(c, end=' ')
        sleep(0.3)
    print('FIM!')

linha(1, 31)
contador(1, 10, 1)
linha(1, 31)
contador(10, 1, 2)
linha(2, 15)
print(f'{'SUA VEZ':^30}')
ini = int(input(f'{'Início:':<8}'))
fim = int(input(f'{'Fim:':<8}'))
passo = int(input(f'{'Passo:':<8}'))
contador(ini, fim, passo)

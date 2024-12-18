# minha versão
# eu não pensei que era para que o menu de opçoes aparecesse mais de uma vez para cada par de números digitados
n1 = n2 = esc = 0
while esc != 5:
    try:
        n1 = int(input('Digite um número inteiro: '))
        n2 = int(input('Digite outro inteiro: '))
        esc = int(input(f"""Qual operação deseja realizar entre {n1} e {n2}?
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Sua opção: """))
    except ValueError:
        print('Digite uma opção válida.')
        continue
    else:
        if esc == 1:
            print(f'A soma de {n1} e {n2} é {n1 + n2}.')
        elif esc == 2:
            print(f'O produto de {n1} e {n2} é {n1 * n2}.')
        elif esc == 3:
            print(f'{n1} é maior.' if n1 > n2 else (f'{n2} é maior.' if n2 > n1 else 'Ambos os números são iguais'))
        elif esc == 4:
            print('E lá vamos nós de novo.')
        elif esc == 5:
            print('Saindo...')
        else:
            print('Digite uma opção válida.')
    print('-' * 25)

# guanabara
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print("""[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa""")
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, soma))
    elif opcao == 2:
        multi = n1 * n2
        print('A multiplicação de {} com {} é {}.'.format(n1, n2, multi))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('{} é o maior.'.format(maior))
    elif opcao == 4:
        print('Iforme os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Saindo...')
    else:
        print('Opção inválida, tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa, volte sempre.')

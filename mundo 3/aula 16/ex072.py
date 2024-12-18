# minha versão
extenso = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    try:
        num = int(input('Digite um número de 0 a 20: '))
    except ValueError:
        print('Precisa ser um número.', end=' ')
    else:
        if 20 < num or num < 0:
            print('Tente novamente.', end=' ')
        else:
            break
print(f'{num} por extenso é {extenso[num - 1]}.')       # eu esqueci de colocar o zero na tupla, por isso o '-1'

# guanabara
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20:  # o mesmo que 'if 20 >= num >= 0:'
        break
    print('Tente novamente.', end=' ')
print(f'Você digitou o número {extenso[num]}.')

# guanabara alternativo
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = -1
while 20 < num or num < 0:  # o teste lógico se repete dentro do while com o mesmo teste, não compensa fazer assim
    num = int(input('Digite um número de 0 a 20: '))
    if 20 < num or num < 0:
        print('Tente novamente.', end=' ')
print(f'Você digitou o número {extenso[num]}.')

# desafio extra
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
esc = ' '
while esc not in 'N':
    while True:
        try:
            num = int(input('Digite um número de 0 a 20: '))
        except ValueError:
            print('Precisa ser um número.', end=' ')
        else:
            if 20 < num or num < 0:
                print('Tente novamente.', end=' ')
            else:
                break
    print(f'{num} por extenso é {extenso[num]}.')
    while True:
        esc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if esc not in 'SN':
            print('Opção inválida.', end=' ')
        else:
            break
print('Encerrando programa...')

def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print('\033[31mERRO! Digite um número INTEIRO válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num


def leiareal(msg):
    while True:
        try:
            num = float(input(msg))
        except ValueError:
            print('\033[31mERRO! Digite um número REAL válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num

inteiro = leiaint('Digite um número INTEIRO: ')
real = leiareal('Digite um número REAL: ')
print(f'O número INTEIRO digitado foi {inteiro} e o REAL foi {real}.')

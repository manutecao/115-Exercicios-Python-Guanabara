def leiaint(enum):
    while True:
        num = input(enum).strip()
        if num.isnumeric():
            num = int(num)
            return num
            # noinspection PyUnreachableCode
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')

n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
num = int(input('Digite um número inteiro: '))
print("""Escolha a base para conversão:
[1] para binário
[2] para octal
[3] para hexadecimal""")
esc = int(input('Sua escolha: '))
if esc == 1:
    conv = bin(num)
    tipo = 'binário'
elif esc == 2:
    conv = oct(num)
    tipo = 'octal'
elif esc == 3:
    conv = hex(num)
    tipo = 'hexadecimal'
else:
    print('Opção inválida. Tente novamente.')
if (esc == 1) or (esc == 2) or (esc == 3):
    print(f'O valor {num} valor convertido em {tipo} é {conv[2:]}.')

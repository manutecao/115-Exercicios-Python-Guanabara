def erro(valor):
    print(f'\033[31mERRO! \'{valor}\' não é um preço válido.\033[m')

def leiadinheiro(msg):
    while True:
        valor = input(msg).strip()
        if  ',' in valor:
            aux = valor.replace(',', '')     # troca a vírgula por nada
            if aux.isnumeric():
                valor2 = valor.replace(',', '.')# troca a vírgula por ponto
                return float(valor2)
            else:
                erro(valor)
        elif '.' in valor:
            aux = valor.replace('.', '')  # troca o ponto por nada
            if aux.isnumeric():
                return float(valor)
            else:
                erro(valor)
        elif  valor.isnumeric():
            return  float(valor)
        else:
            erro(valor)

def leiadinheiro2(msg):
    """
    Essa função ainda dá erro quando o 'input' é alfanumérico como: '123f'
    :param msg:
    :return:
    """
    valido = False
    while not valido:
        entrada = str(input(msg)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO: Entrada \'{entrada}\' é um preço inválido.\033[m')
        else:
            valido = True       # se o 'return' da 'break', não é necessário esse
            return float(entrada)   # teste lógico, mais fácil usar um 'while True'

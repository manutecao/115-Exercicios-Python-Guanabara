from outros import *
from time import sleep

def menu(txt, opc):
    """ Mostra um menu na tela e coleta a opção escolhida:
    ------------------------------
            MENU PRINCIPAL
    ------------------------------
     1 - Ver pessoas cadastradas
     2 - Cadastrar nova Pessoa
     3 - Sair do Sistema
    ------------------------------
    Sua opção: 1
    ------------------------------
    :param txt: Título do menu 'str'
    :param opc: Lista com as opções 'str' a serem disponibilizadas no menu.
    :return: A opção escolhida 'int'.
    """
    if opc is None:
        opc = list()
    titulo(txt)
    for op in range(0, len(opc)):
        print(f' {op + 1} - \033[34m{opc[op]:<23}\033[m')
    linha(1, 30)
    #while True:
    esc = leiaint('Sua opção: ', escopo=True, piso=1, teto=3)
    return esc

def ver():
    """ Mostra uma tabela com as pessoas cadastradas no arquivo 'teste.txt'.
    ------------------------------
          PESSOAS CADASTRADAS
    ------------------------------
    NOME                 | IDADE
    Pessoa 1             | 23
    Pessoa 2             | 24
    Pessoa 3             | 4
    :return:
    """
    try:
        txt = open('teste.txt', 'r')
    except FileNotFoundError:
        vermelho('Arquivo de registro não encontrado.')
        print('Cadastre uma pessoa para criá-lo.')
    else:
        titulo('PESSOAS CADASTRADAS')
        print(f'{'NOME':<21}| {'IDADE':<7}')
        for p in txt:
            pessoa = p.split(':')
            print(f'{pessoa[0]:21}| {pessoa[1].replace('\n','')}')
            pessoa.clear()
        sleep(3)

def cadastrar():
    """ Registra os dados nome e a idade separados por ':'
        no final do arquivo 'teste.txt'.
        Obs: Cria o arquivo se não existir.
    Pessoa1:23
    Pessoa2:24
    Pessoa3:4
    :return:
    """
    titulo('NOVO CADASTRO')
    while True:
        try:
            nome = str(input('\033[32mNome: \033[m')).strip()
        except KeyboardInterrupt:
            interrompeu()
            nome = ''
            break
        else:
            if nome == '':
                print('Por favor, digite o nome.')
            else:
                if not nome.isalpha():
                    vermelho('Nomes contém apenas letras.')
                else:
                    break
    while True:
        try:
            idade = leiaint('Idade: ', escopo=True, piso=0, teto=150)
        except KeyboardInterrupt:
            interrompeu()
        else:
            if idade < 0:
                vermelho('Não é possível uma pessoa ter idade negativa.')
            else:
                break
    if nome == '' and idade == 0:
        print('Nenhum registro foi adicionado.')
    else:
        txt = open('teste.txt', 'a')
        txt.write(f'{nome}:{idade}\n')
        txt.close()
        print(f'Novo registro de \'{nome}\' adicionado.')
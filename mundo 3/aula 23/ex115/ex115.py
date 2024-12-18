from modulos import *
from outros import *

while True:
    opc = menu('MENU PRINCIPAL',
               ['Ver pessoas cadastradas',
                    'Cadastrar nova Pessoa',
                    'Sair do Sistema'],)
    if opc == 0:    # KeyboardInterruptError
        sair()
        break
    elif opc == 1:
        ver()
    elif opc == 2:
        cadastrar()
    elif opc == 3:
        sair()
        break
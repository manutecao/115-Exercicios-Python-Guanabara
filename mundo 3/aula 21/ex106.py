def titulo(title, fc=97, bc=49):
    """
    --> Estiliza um texto para formato de título
    :param title: texto a ser colocado no título
    :param fc:    cor da FONTE
    :param bc:    cor de FUNDO
    :return:
    """
    print(f'\033[{fc}:{bc}m' + '-' * (len(title) + 4)  + '\033[m')
    print(f'\033[{fc}:{bc}m' + f'  {title}  ' + '\033[m')
    print(f'\033[{fc}:{bc}m' + '-' * (len(title) + 4) + '\033[m')

def ajuda(text, fc=97, bc=49):
    print(f'\033[{fc}:{bc}m', end='')
    help(text)
    print(f'\033[m', end='')

item = ' '
while True:
    titulo('Sistema de ajuda PyHelp', 30, 103)
    item = input('Função ou Biblioteca > ').strip()
    if item.upper() in 'FIM':
        break
    titulo(f'Acessando o manual do comando \'{item}.\'', 30,104,)
    ajuda(item, fc=30, bc=47)
titulo('Até Logo!', 97,41)

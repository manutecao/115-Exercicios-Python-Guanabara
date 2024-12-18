from urllib.request import urlopen
from urllib.error import *

# como atualmente o website 'https://www.pudim.com.br/'
# tem problemas com certificar SSL,
# vou testar a conectividade de outro website qualquer

try:
    html = urlopen('https://radiooooo.com/')
except HTTPError as e:
    print('Não consegui verificar conexão com o site https://radiooooo.com/')
except URLError as e:
    print('Não consegui verificar conexão com o site https://radiooooo.com/')
else:
    print('O site https://radiooooo.com/ está funcionando.')

# guanabara
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://radiooooo.com/')
except urllib.error.URLError:
    print('O site "https://radiooooo.com/" não está acessível no momento.')
else:
    print('Consegui acessar o site "https://radiooooo.com/" com sucesso.')
    print(site.read())
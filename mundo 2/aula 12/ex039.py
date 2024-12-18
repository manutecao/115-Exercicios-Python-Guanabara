from datetime import date

# minha versao
ano = int(input('Qual é o seu ano de nascimento? '))
atual = date.today().year
idade = atual - ano
data = date.today()
print(f'Se você nasceu em {ano}, em {atual} sua idade é {idade}.')
if idade < 18:
    print('Aproveita que com 18 anos tu tem que alistar.')
    # prev = ano + 18
    # ainda = prev - data.year
    # print(f'Ainda faltam {ainda} anos pra tu alistar, pode relaxar kkkkk')
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos pra tu alistar, pode relaxar kkkkk')
    print(f'Seu alistamento obrigatório será em {ano + 18}.')
elif idade == 18:
    print('Iiiixi, já é obrigado a alistar kkkkkkkkk.')
    fim = date(2024,12,31)
    rest = (fim - data).days # tenho que aprender como determina o formato disso aqui
    print(f'Fica esperto que faltam só {rest} dias pra tu alistar. kkkkkk')
elif idade > 18:
    print('Você está atrasado para o alistamento.')
    # aux = ano + 18
    # ini = date( aux,1,1)
    # jafoi = (data - ini).days
    # print(f'Tu tá só {jafoi} dias atrasado kkkkkk')
    saldo = idade - 18
    print(f'Seu alistamento foi em {ano + 18}.')
    print(f'Tu tá só {saldo} anos atrasado kkkkkk')


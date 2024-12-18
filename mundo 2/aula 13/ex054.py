from datetime import date

nomes = ['','','','','','','']              # agora que eu parei pra pensar que não precisava armazenar nada....
anos = [0,0,0,0,0,0,0]
for c in range(0,6):
    nomes[c] = str(input(f'Digite o nome da {c + 1}ª pessoa: '))
    anos[c] = input(f'Digite o ano de nascimento da {c + 1}ª pessoa: ')
# print(nomes)
# print(anos)
idades = [0,0,0,0,0,0,0]                            # (1) ele não pediu isso
maioridade = [False,False,False,False,False,False]  # (1)
atual = date.today().year
demenor = 0
demaior = 0
for c in range(0,6):
    idades[c] = int(atual) - int(anos[c])
    if idades[c] < 18:
        demenor += 1
    elif idades[c] >= 18:
        demaior += 1
print('')
print(f'Ao final {demenor} pessoas ainda não atingiram a maioridade e {demaior} já atingiram.')
print('')
for c in range(0,6):                            # (1)
    print(f'{nomes[c]:<12}| Nasc. {anos[c]:^4} | Idade {idades[c]} | De maior: {maioridade[c]}')

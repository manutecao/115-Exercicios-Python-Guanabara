from datetime import date

totmaior = 0
totmenor = 0
atual = date.today().year
for c in range(1,8):
    nasc = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = atual - nasc
    # print(idade)
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao final {totmenor} pessoas ainda não atingiram a maioridade e {totmaior} já atingiram.')
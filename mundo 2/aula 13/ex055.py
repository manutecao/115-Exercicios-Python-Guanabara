pesos = [0,0,0,0,0]     # ainda sim, em nenhum momento ele pediu para armazenar nada, de novo...
for c in range(0,5):
    pesos[c] = float(input(f'Digite o número da {c + 1}ª pessoa (em Kg): '))
#print(pesos)
pesos.sort()                     # eu to cansado, desculpa
#print(pesos)
print(f'O MENOR peso é {pesos[0]} Kg, enquanto o MAIOR é {pesos[-1]} Kg')
print('')

filtrados = [9,8,7,6,5,4]
print(filtrados)                # mas tb não quer dizer que eu não consiga
aux = 0
for c in range(0, 5):
    for b in range(c + 1, 6):
        if filtrados[c] > filtrados[b]:
            aux = filtrados[c]
            filtrados[c] = filtrados[b]
            filtrados[b] = aux
print(filtrados)
print('')

# guanabara
peso = 0
maior = 0
menor = 9999    # <--- isso não é aconselhável
for c in range(1,6):
    peso = float(input(f'Digite o número da {c}ª pessoa (em Kg): '))
    if c == 1:          # guanabara indica fazer isso aqui ao invés de colocar o menor como um número gigante (9999999)
        maior = peso
        menor = peso
                                            # print(f'Maior {maior}, menor {menor}')
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O MENOR peso é {menor} Kg, enquanto o MAIOR é {maior} Kg')

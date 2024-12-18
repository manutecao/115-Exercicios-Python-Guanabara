somador = 0
cont = 0
for num in range(1,501,2): # passo 2 é bom que ele skipa os pares, economizando processamento
    if num % 3 == 0:    # se ele só vai processar os ímpares, não tem pq verificar ( num % 2 == 0 )
        # print(num)
        somador += num
        cont += 1
print(f"""A soma de todos {cont} os números ímpares e multiplos de 3
entre 1 e 500 é {somador}.""")

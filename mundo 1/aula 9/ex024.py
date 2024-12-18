# minha versao ( eu juro que não consegui pensar em outra maneira senao usando o estrutura condicional )
# errei por nao ler o enunciado direito, se eu soubesse que "santo" tinha que ser o primeiro nome...

nome = input('Digite o nome da cidade: ') # podia ter usado o .strip() ja logo na entrada do nome
achou = nome.strip().upper().find('SANTO')
if achou == -1:
    print('O nome dessa cidade não contém a palavra "Santo".')
elif achou == 0:
    print('O nome dessa cidade começa com "Santo".')
else:
    print(f'A palavra "Santo" apareceu, mas na posição {achou},\n logo, não começa com "Santo".')

# guanabara
nome = str(input('Digite o nome da cidade: ')).strip()
print(nome[:5].upper() == 'SANTO')

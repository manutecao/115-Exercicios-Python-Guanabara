lista = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
         'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
#vogais = 'AEIOU'        # nem precisava desa variável

for word in lista:
    print(f'\nNa palavra {word.upper()} temos', end=' ')
    for letra in word:
        if letra.upper() in vogais: # essas vogais só serão utilizadas aqui, logo, poderia ser apenas um 'AEIOU'
            print(letra, end=' ')
#   print('')       # posso apenas quebrar a linha em cada início de laço

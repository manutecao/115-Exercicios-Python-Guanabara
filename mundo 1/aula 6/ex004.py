valor = input('Digie algo: ')
print(f'O que foi digitado é do tipo primitivo de {type(valor)}.')
print(f'Tem {len(valor)} caracteres.')

print(f'Se é alfanumérico: {valor.isalnum()}')
print(f'Se é alfabético: {valor.isalpha()}')
print(f'Foi escrito em minúsculo: {valor.islower()}')
print(f'Foi escrito em maiúculo: {valor.isupper()}')
print(f'Se o valor é um espaço: {valor.isspace()}')
print(f'Está capitalizada? {valor.istitle()}')

print(f'Se é numérico: {valor.isnumeric()}')
print(f'Se é um valor decimal: {valor.isdecimal()}')
from datetime import date
cidadao = {}
cidadao['nome'] = str(input('Nome: ')).strip()
anoNasc = int(input('Ano de nascimento: '))
esseAno = date.today().year
cidadao['idade'] = esseAno - anoNasc
cidadao['ctps'] = int(input('Carteira de trabalho: (0 se não tiver) '))
if cidadao['ctps'] != 0:
    cidadao['anoContrat'] = int(input('Ano de contratação: '))
    cidadao['salario'] = float(input('Salário: '))
    cidadao['idadeAposen'] = (35 - (esseAno - cidadao['anoContrat'])) + cidadao['idade']
for k, v in cidadao.items():
    print(f'{k}: {v}')

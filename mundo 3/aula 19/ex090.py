# minha versão
"""classe = []
nome = str(input('Nome: '))
media = float(input('Média: '))
if media >= 6:
    situacao = 'Aprovado'
elif media >= 4:
    situacao = 'Recuperação'
else:
    situacao = 'Reprovado'
classe.append({'nome':nome,'media':media, 'situacao':situacao})"""
#print(f"""O nome é {classe[0]['nome']}.
#A média é {classe[0]['media']}.
#A situação é {classe[0]['situacao']}.""")

# minha versão 2
aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
if aluno['media'] >= 6:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 4:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print(f"""O nome é {aluno['nome']}.
A média é {aluno['media']}.
A situação é {aluno['situacao']}.""")

# guanabara
aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
if aluno['media'] >= 6:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 4:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-=' * 10)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')

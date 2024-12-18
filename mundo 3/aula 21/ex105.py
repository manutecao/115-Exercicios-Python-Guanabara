def linha(tipo, tam):
    if tipo == 1:
        print('-' * tam)
    elif tipo == 2:
        print('-=' * tam)

def notas(*nota, sit=False):
    """
    --> Função para analisar as notas de um ou mais alunos
    :param nota: para cada 'nota', a nota individual de cada aluno
    :param sit: (opcional) se deseja uma avaliação qualitativa da média da turma
    :return: dicionário com total, maior, menor, média e situação (opcional).
    """
    notasdict = dict()
    notasdict['total'] = len(nota)
    notasdict['maior'] = max(nota)
    notasdict['menor'] = min(nota)
    notasdict['media'] = sum(nota) / len(nota)
    if sit:
        if notasdict['media'] >= 7:
            notasdict['situacao'] = 'BOA'
        elif notasdict['media'] >= 5:
            notasdict['situacao'] = 'RAZOÁVEL'
        else:
            notasdict['situacao'] = 'RUIM'
    return notasdict

linha(1, 20)
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)

def notas(*num, sit=False):
    """
    — > Analisar notas e situações de vários alunos,
    :param num: uma ou mais notas
    :param sit: valor opcional, se deve ou não aparecer
    :return: dicionario com tudo
    """
    resp = {}
    maior = num[0]
    menor = num[0]
    q = len(num)
    m = 0
    for c in range(0, len(num)):
        m += num[c]
        if num[c] > maior:
            maior = num[c]
        elif num[c] < menor:
            menor = num[c]
    media = m / q
    resp['total'] = q
    resp['maior'] = maior
    resp['menor'] = menor
    resp['media'] = media
    if sit:
        if media >= 7:
            situacao = 'BOA'
        elif 7 > media > 6:
            situacao = 'RAZOÁVEL'
        else:
            situacao = 'RUIM'
        resp['situação'] = situacao
    return resp

r = notas(3.5, 2, 6.5, 2, 7, 9, 10, 2, 4.75, sit=True)
print(r)

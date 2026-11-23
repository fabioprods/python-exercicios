def aumentar(valor, porcento,formato=False):
    r = valor + (valor * porcento / 100)
    if formato:
        return nota (r)
    else:
        return r
def diminuir(valor, porcento,formato=False):
    r = valor - (valor * porcento / 100)
    if formato:
        return nota (r)
    else:
        return r
def dobro(valor,formato=False):
    r = valor * 2
    if formato:
        return nota (r)
    else:
        return r
def metade(valor,formato=False):
    r = valor / 2
    if formato:
        return nota (r)
    else:
        return r

def nota(valor):
    return f'R${valor:.2f}'.replace('.', ',')

def resumo(valor,porcento1, porcento2):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'{"Preço analisado:":<20}{nota(valor)}')
    print(f'{"Dobro do preço:":<20}{dobro(valor,formato=True)}')
    print(f'{"Metade do preço:":<20}{metade(valor,formato=True)}')
    print(f'{f"{porcento1}% de aumento:":<20}{aumentar(valor,porcento1,formato=True)}')
    print(f'{f"{porcento2}% de redução:":<20}{diminuir(valor,porcento2,formato=True)}')
    print('-' * 30)

from utilidades.moeda import moeda
from utilidades.dado import dado

valor = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(valor,35,22)

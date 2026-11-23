tudo = {}
galera = []
while True:
    total = 0
    gols = []
    nome = input('Qual o nome do jogador?: ')
    partidas = int(input(f'Quantas partidas o {nome} jogou?: '))
    for c in range(1, partidas+1):
        numero = int(input(f'Quantos gols na partida {c}?'))
        total += numero
        gols.append(numero)
    tudo['nome'] = nome
    tudo['gols'] = gols[:]
    tudo['total'] = total
    galera.append(tudo.copy())
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('-' * 30)
    if continuar == 'N':
        break
print('cod  nome        gols         total')
print('-' * 30)
for pos, valor in enumerate(galera):
    print(f'{pos} {valor["nome"]} {valor["gols"]} {valor["total"]} ')
print('-' * 30)
codigo = 0
while True:
    codigo = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if codigo == 999:
        break
    if codigo >= len(galera):
        print('Jogador não encontrado!')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {galera[codigo]["nome"]}')
        for pos, gols in enumerate(galera[codigo]['gols']):
            print(f'No jogo {pos + 1} fez {gols} gols')
        print('-' * 30)
print('<< VOLTE SEMPRE >>')

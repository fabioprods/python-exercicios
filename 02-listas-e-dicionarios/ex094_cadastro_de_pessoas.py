pessoa = {}
galera = []
media2 = 0
pessoas = 1
mulheres = []
while True:
    nome = str(input('Digite seu nome: '))
    sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
    idade = int(input('Digite sua idade: '))
    pessoa['nome'] = nome
    pessoa['sexo'] = sexo
    pessoa['idade'] = idade
    galera.append(pessoa.copy())
    media2 += idade
    if sexo == 'F':
        mulheres.append(nome)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
    elif continuar == 'S':
        pessoas += 1
media = media2 / pessoas
print(galera)
print('-=' * 30)
print(f'O grupo tem {pessoas} pessoas.')
print(f'A média de idade é de {media:.2f} anos.')
print(f'As mulheres cadastradas foram: {mulheres}')
print('Lista de pessoas acima da media: ')
for p in galera:
    if p['idade'] > media:
        print(f'Nome = {p["nome"]}; Sexo = {p["sexo"]}; Idade = {p["idade"]}')

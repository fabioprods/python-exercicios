aluno = []
op = 'S'
nt = []
nota = nota1 = consulta = 0
todos = []
while op == 'S':
    aluno.append(str(input('Nome: ')))
    nota = float(input('Nota 1: '))
    nt.append(nota)
    nota1 = float(input('Nota 2: '))
    nt.append(nota1)
    aluno.append(nt[:])
    aluno.append((nota + nota1)/2)
    op = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    nt.clear()
    todos.append(aluno[:])
    aluno.clear()
print('-=' * 30)
print('No.    NOME    MÉDIA')
for pos, valor in enumerate(todos):
    print(f'{pos}    {valor[0]}    {valor[2]}')
while consulta != 999:
    consulta = int(input('Mostrar as notas de qual aluno? (999 interrompe)'))
    if consulta == 999:
        break
    if consulta >= len(todos):
        print('Aluno não encontrado')
        continue
    print(f'As notas de {todos[consulta][0]} são {todos[consulta][1]}')

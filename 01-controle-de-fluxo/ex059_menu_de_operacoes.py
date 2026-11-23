import time
p = 0
n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero inteiro: '))
while p != 5:
    p = int(input('Escolha uma opção: \n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair do programa\n'))
    if p == 1:
        print(f'A soma dos números é {n1 + n2}')
        time.sleep(1)
    elif p == 2:
        print(f'O resultado da multiplicação é {n1 * n2}')
        time.sleep(1)
    elif p == 3:
        if n1 > n2:
            print(f'O maior numero é {n1}')
            time.sleep(1)
        elif n1 < n2:
            print(f'O maior numero é {n2}')
            time.sleep(1)
        else:
            print('É um empate')
            time.sleep(1)
    elif p == 4:
        n1 = int(input('Digite um numero inteiro: '))
        n2 = int(input('Digite outro numero inteiro: '))
        time.sleep(1)
    elif p == 5:
        print('Finalizando...')
    else:
        print('Opção invalida!')
        time.sleep(1)

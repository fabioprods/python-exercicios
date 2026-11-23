def leiaInt1(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Informe um numero Inteiro')
        except KeyboardInterrupt:
            print('\nO usuário preferiu nao informar os dados!')
            return 0
        else:
            return num

def leiaFloat1(msg):
    while True:
        try:
            num1 = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Informe um numero Real')
        except KeyboardInterrupt:
            print('\nO usuário preferiu nao informar os dados!')
            return 0
        else:
            return num1

num = leiaInt1('Digite um numero Inteiro: ')
num1 = leiaFloat1('Digite um numero Real: ')
print(f'O valor inteiro digitado foi {num} e o real foi {num1}')

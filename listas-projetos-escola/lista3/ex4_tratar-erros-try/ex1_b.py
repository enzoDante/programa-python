from math import pow
while True:
    try:
        print('-'*30)
        print('1- QUADRADO DE UM NÚMERO\n2- raiz cúbica de um número\n3- fatorial de um número\n')
        escolha = int(input('Escolha uma opção acima!!!\n'))
        while escolha < 1 or escolha > 3:
            escolha = int(input('Digite um número apresentado no menu!!!\n'))
        if escolha == 1:
            num = int(input('Digite um número: '))
            print(f'O quadrado de {num} é {num**2}')
        elif escolha == 2:
            num = int(input('Digite um número: '))
            print(f'a raiz cúbica de {num} é {pow(num, 1/3):.2f}')
        else:
            num = int(input('Digite um número: '))
            f = 1
            for i in range(1, num+1):
                f *= i
            print(f'Fatorial de {num} é {f}')

    except (ValueError):
        print('='*55)
        print('Não digite nada além dos números das opções ou \nnúmeros para cálculos escolhidos!!!')
        print('='*55,'\n')
    else:
        break
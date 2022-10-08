def primon(num):
    cont = 0
    print(f'Verificando se o número digitado é primo!!!')
    for x in range(1, num+1):
        if num % x == 0:
            cont += 1
    if cont == 2:
        print(f'{num} é primo')
    else:
        print(f'{num} não é primo')


n = int(input('Digite um número:\n'))
primon(n)
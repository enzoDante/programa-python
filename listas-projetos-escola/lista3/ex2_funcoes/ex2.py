def somatorio(n):
    '''
    ira calcular o somatorio do numero passado como parametro
    retornara o valor do somatorio e se a variavel 'ver' for verdadeira, ira retornar uma mensagem do passo a passo desse somatorio feito
    :param n:
    :return s ou msg: se ver = True exemp(n=4): 1+2+3+4 = 10| se ver = False exemp(n=4): 10 
    '''
    s = 0
    msg = ""
    for i in range(1, n+1):
        s += i
        if i < n:
            msg += f'{i} + '
        else:
            msg += f'{i} = {s}'
    if ver:
        return msg
    else:
        return s
help(somatorio)
while True:
    ver = False
    num = int(input('Digite um número: '))
    while num < 0:
        num = int(input('Digite um número positivo: '))

    escolha = input('Deseja visualizar o processo da soma? s:')
    if escolha.upper() == 'S':
        ver = True

    print(somatorio(num))

    if int(input('deseja continuar? 1-sim/qualquer número-não\n')) != 1:
        break

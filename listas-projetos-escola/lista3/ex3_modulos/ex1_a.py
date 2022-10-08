import TESTE
#help(TESTE)
num = list()
while True:
    for i in range(0, 11):
        n = int(input(f'{i+1}º digito do cpf '))
        while n < 0 or n > 9:
            n = int(input(f'{i+1}º digito do cpf '))
        num.append(n)

    print(TESTE.Valida_CPF(num))
    num.clear()
    if int(input('deseja continuar? 1-sim/qualquer número-não\n')) != 1:
        break
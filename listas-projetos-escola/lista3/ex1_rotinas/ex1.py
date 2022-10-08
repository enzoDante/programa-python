
def bina():
    binario = ""
    print(f'numero: {n} para binário = ')
    num = n
    while True:
        valor_bin = num % 2
        num = num // 2
        binario += f'{valor_bin}'
        if num < 1:
            break
    print(binario)


n = int(input("Digite um número:\n"))
bina()
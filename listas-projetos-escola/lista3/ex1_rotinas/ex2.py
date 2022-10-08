
def bina(num=0):
    binario = ""
    print(f'numero: {num} para binário = ')
    while True:
        valor_bin = num % 2
        num = num // 2
        binario += f'{valor_bin}'
        if num < 1:
            break
    print(binario)


n = int(input("Digite um número:\n"))
bina(n)
bina(59)
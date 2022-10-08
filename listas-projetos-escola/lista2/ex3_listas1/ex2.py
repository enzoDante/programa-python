lista = list()

i = 0
while True:
    i += 1
    num = int(input(f'Digite {i}º número: '))
    if num == 0:
        break
    while num in lista:
        num = int(input('Digite um número que não esteja na lista!!!\n'))
    lista.append(num)
print(lista)
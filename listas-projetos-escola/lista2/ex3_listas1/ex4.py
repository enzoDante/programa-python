lista = list()
par = list()
impar = list()
for i in range(0, 8):
    num = int(input(f'Digite {i+1}º número: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
for i in range(0, 7):
    for x in range(0, 7):
        if lista[x] < lista[x+1]:
            aux = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = aux

print(f'Lista original:\n{lista}')
print(f'lista de pares:\n{par}')
print(f'lista de impares:\n{impar}')
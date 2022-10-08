lista = list()

for i in range(0, 10):
    num = int(input(f'Digite {i+1}º número: '))
    while num in lista:
        num = int(input('Digite um número que não esteja na lista:  '))
    lista.append(num)
print(lista)
print('\n\n')


for i in range(0, 9):
    for x in range(0, 9):
        if lista[x] > lista[x+1]:
            aux = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = aux




for i, v in enumerate(lista):
    print(f'[{v}] na posição [{i}]')

print('\n\n')
print(lista)


"""ativo = 1
while ativo == 1:
    ativo = 0
    for i in range(0, 9):
        if lista[i] > lista[i+1]:
            ativo = 1
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux"""
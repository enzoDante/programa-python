n = int(input())
lista = list()
a = 1
letra = ''
frase = ''
for i in range(0, n):
    x = str(input())
    x += ' '
    for z in range(0, len(x)-1):
        if x[z] == x[z+1]:
            a += 1
        else:
            frase += "{}{}".format(a,x[z])
            a = 1
    lista.append(frase)
    frase = ''
for i in range(0, len(lista)):
    print(lista[i])
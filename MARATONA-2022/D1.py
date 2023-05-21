n = int(input())
lista = list()
a = ''
letra = ''
frase = ''
for i in range(0, n):
    x = str(input())
    for z in range(0, len(x)):
        teste = x.count(x[z])
        letra = x[z]
        if not letra == a:
            c = "{}{}".format(teste,x[z])
            frase += c
            a = letra
    #print(lista)
    lista.append(frase)
    frase = ''
for z in range(0, len(lista)):
    print(lista[z])
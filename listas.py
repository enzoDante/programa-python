lista = ['alface', 'cebola', 'laranja', 'macarrão', 'cenoura']
print(lista) #irá printar a lista
for i in lista:
    print(i) #irá printar os elementos
             #linha por linha!

print(len(lista))#5 elementos
lista.append('bolo')#adiciona 'bolo' na lista
print(lista, len(lista)) #6 elementos

lista.insert(2, 'suco') #adiciona'suco' na posição 0
print(lista, len(lista))#ele n remove o q está na posição 0!

lista.remove('bolo')#remove 'bolo' da lista
print(lista)

av = lista.pop()#remove um elemento e retorna ele
print(f'{lista}\n{av}')

axs = lista.index('alface')#mostra a posição do elemento
print(axs)

x = lista.count('alface')#quantas vezes aparece tal elemento
print(x)

s = lista.sort()#ordena a lista, ordem do alfabeto

lista.reverse()#reverte a lista
print(lista)
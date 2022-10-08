palavras = ['Casa','gato','cachorro','objeto']

for x in palavras:
    print(x, len(x))

for x in range(5):
    print(x) # irá printar: "0 1 2 3 4"
print(len(palavras))

nomes = ['João', 'lucas', 'mateus', 'outros']
for x in range(len(nomes)):
    print(x, nomes[x])

sum(range(4)) #vai somar '0+1+2+3'
print(sum(range(4)))

c = 0
while True:
    c+=1
    pass#serve p continuar o loop mesmo vazio!!!
    if c ==10:
        break


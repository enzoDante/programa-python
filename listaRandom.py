import random
lista = []
x = 0
esc = input("deseja inserir letra?").upper()
if esc == 'SIM' or esc == 'S':
    este = int(input("quantos deseja adiconar?"))
while esc == 'SIM' or esc == 'S':
    inserir = input("insira uma letra: ")
    lista.append(inserir)
    x += 1
    if x >= este:
        esc = input("deseja inserir outra letra?").upper()

random.shuffle(lista)
for x in lista:
    print(x)

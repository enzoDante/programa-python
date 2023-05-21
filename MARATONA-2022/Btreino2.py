n = int(input())
nome = list()
for x in range(0, n):
    nome.append(input())
for i in range(0, len(nome)):
    for x in range(0, len(nome)):
        if not nome[i] == nome[x]:
            print(i+1,nome[i],"x",nome[x])

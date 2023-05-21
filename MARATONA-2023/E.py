#==========INCORRETO========
#apesar de funcionar exatamente como a questão pede
#o sistema diz estar incorreto
n = int(input())
resp = list()

for i in range(0, n):
    y = list()
    x = list()
    for l in range(0, 2):
        y.append(int(input()))
        x.append(int(input()))
    if x[0] == x[1]:
        resp.append(y[1] - y[0])
    elif y[0] == y[1]:
        resp.append(x[1] - x[0])
    else:
        resp.append("FA")

for i in resp:
    print(i)

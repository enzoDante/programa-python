#======não foi entregue=====
#programa funciona exatamente como foi pedido, mas n foi enviado ao sistema
#não sei se o sistema aceitaria o programa como correto!
n = int(input())
times = list()
fase = 0
resp = list()

for i in range(0, n):
    times.append(input())
times.sort()
for i in range(0, n):
    resp.append("{}o. Fase".format(i+1))
    for l in range(0, n):
        if i != l:
            resp.append("{} x {}".format(times[i], times[l]))

for i in resp:
    print(i)
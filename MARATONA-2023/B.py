#não entregue --- não entendi a lógica matemática de como fazer
#fibonacci
import math
n = int(input())
resp = list()
for i in range(0, n):
    alfa = int(input())
    raio = int(input())

    x = 400 + raio * math.cos((alfa * math.pi)/180)
    y = 400 + raio * math.sin((alfa * math.pi)/180)
    resp.append("{:.0f},{:.0f}".format(x, y))

for i in resp:
    print(i)
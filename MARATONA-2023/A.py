#==========CORRETO========
n = int(input())

resp = list()

for i in range(0, n):
    x = int(input())
    y = int(input())
    z = int(input())

    if x + y + z == 180:
        resp.append("S")
    else:
        resp.append("N")

for i in resp:
    print("{}".format(i))

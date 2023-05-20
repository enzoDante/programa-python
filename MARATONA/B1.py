n = int(input())

resp = list()
for i in range(0, n):
    x = list()
    x2 = list()
    y2 = list()
    z2 = list()
    d1 = list()
    d2 = list()
    x2.append(int(input()))
    x2.append(int(input()))
    x2.append(1)
    y2.append(int(input()))
    y2.append(int(input()))
    y2.append(1)
    z2.append(int(input()))
    z2.append(int(input()))
    z2.append(1)
    x.append(x2)
    x.append(y2)
    x.append(z2)

    d1.append(x[0][0] * x[1][1] * x[2][2])
    d1.append(x[0][1] * x[1][2] * x[2][0])
    d1.append(x[0][2] * x[1][0] * x[2][1])

    d2.append(x[2][0] * x[1][1] * x[0][2])
    d2.append(x[2][1] * x[1][2] * x[0][0])
    d2.append(x[2][2] * x[1][0] * x[0][1])
    j = (d1[0] + d1[1] + d1[2]) - (d2[0] + d2[1] + d2[2])
    resp.append(j)
    del x2
    del y2
    del z2
    del x
    
for i in range(0, n):
    if resp[i] == 0:
        print('S')
    else:
        print('N',resp[i])



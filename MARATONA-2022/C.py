n = int(input())
x = list()
for i in range(0, n):
    nf = int(input())
    ni = int(input())
    d = int(input())
    t= 0
    while ni <= nf:
        ni+=d
        t+=1
    x.append(t)
for i in range(0, n):
    print(x[i])
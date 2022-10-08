n = int(input())
x = list()
a = 0

for i in range(0, n):
    x.append(int(input()))
for i in range(6, 0, -1):
    todos = x.count(i)
    a = i
    if todos > 0:
        print("{} = {}/{}".format(a,todos,n))
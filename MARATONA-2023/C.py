#==========CORRETO========
n = int(input())

a = ''
string = input()
for i in range(0, n):
    a += string[i]

tt = a.split("b")
x = 0
for i in tt:
    if i != '' and i.count("a") > 1:
        x += i.count('a')
print(x)
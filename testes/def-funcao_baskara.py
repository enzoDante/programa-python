import math
def temR(a,b,c):
    delta = (b*b) -4*a*c
    return delta

def raiz01(a,b,c,delta):
    raiz1 = (-b + math.sqrt(delta))/(2*a)
    return raiz1
def raiz02(a,b,c,delta):
    raiz2 = (-b - math.sqrt(delta))/(2*a)
    return raiz2

a = int(input("digite A: "))
b = int(input("digite B: "))
c = int(input("digite C: "))
delta = temR(a,b,c)
if delta >= 0:
    raizx1 = raiz01(a,b,c, delta)
    raizx2 = raiz02(a,b,c,delta)
    print(raizx1)
    print(raizx2)
else:
    print("Não tem raizes!!!")
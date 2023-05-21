import math

resp = list()
vezes = int(input())

for i in range(0, vezes):
    x = list()
    y = list()
    
    for l in range(0, 3):
        x.append(int(input()))
        y.append(int(input()))
    
    #reta1 = math.sqrt(x[1] - x[0]) + math.sqrt(y[1] - y[0])
    reta1 = ((x[1] - x[0])**2) + ((y[1] - y[0]) **2) **(1/2)
    reta2 = ((x[1] - x[2])**2) + ((y[1] - y[2]) **2) **(1/2)
    reta3 = ((x[2] - x[0])**2) + ((y[2] - y[0]) **2) **(1/2)
    print(reta1)
    print(reta2)
    print(reta3)

    t1 = abs(reta2 - reta3) < reta1 and reta1 < reta2 + reta3
    t2 = abs(reta1 - reta3) < reta2 and reta2 < reta1 + reta3
    t3 = abs(reta1 - reta2) < reta3 and reta3 < reta1 + reta2

    if t1 and t2 and t3:
        print('forma')
    else:
        print('n forma')
    if reta1 + reta2 < reta3 and reta1 + reta3 < reta2 and reta2 + reta3 < reta3:
        print('forma uma reta')
    else:
        print('n forma uma reta')

#era p funcionar!
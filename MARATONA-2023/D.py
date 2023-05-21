#==========CORRETO========
n = int(input())
resp = list()
teste = ""
for i in range(0, n):
    z1 = input()
    z2 = input()

    val = list()
    val2 = list()
    string = ""
    for l in range(0, len(z1)):
        if z1[l] == "-":
            string += z1[l]
        elif l > 0 and (z1[l-1] == "-" or z1[l-1] == "+") and z1[l] == "i":
            string += '1'
            val.append(string)
            string = ''
        elif z1[l] != "i" and z1[l] != "+":
            string += z1[l]
            if z1[l+1] not in "0123456789":
                val.append(string)
                string = ""
    
    string = ""
    for l in range(0, len(z2)):
        if z2[l] == "-":
            string += z2[l]
        elif l > 0 and (z2[l-1] == "-" or z2[l-1] == "+") and z2[l] == "i":
            string += '1'
            val2.append(string)
            string = ''
        elif z2[l] != "i" and z2[l] != "+":
            string += z2[l]
            if z2[l+1] not in "0123456789":
                val2.append(string)
                string = ""
    
    s1 = int(val[0]) + int(val2[0])
    s2 = int(val[1]) + int(val2[1])

    s3 = int(val[0]) - int(val2[0])
    s4 = int(val[1]) - int(val2[1])

    if s2 >= 0:
        a = "({}+{}i)".format(s1, s2)
    else:
        a = "({}{}i)".format(s1, s2)
    if s4 > 0:
        b = "({}+{}i)".format(s3, s4)
    else:
        b = "({}{}i)".format(s3, s4)
    resp.append(a)
    resp.append(b)

for i in resp:
    print(i)


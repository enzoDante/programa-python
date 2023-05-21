cobras = [[14, 4], [19, 8], [22, 20], [24, 16]]
escadas = [[3, 11], [6, 17], [9, 18], [10, 12]]

resp = list()
cobraXescada = False

jogadores = int(input())

for i in range(0, jogadores):
    dados = int(input())
    casaAtual = int(input())

    if dados > 6:
        resp.append('N')
    else:
        for l in cobras:
            if casaAtual == l[0]:
                resp.append(l[1])
                cobraXescada = True
        for l in escadas:
            if casaAtual == l[0]:
                resp.append(l[1])
                cobraXescada = True
                
        if not cobraXescada:
            
            if casaAtual + dados > 25:
                resp.append('I')
            elif casaAtual + dados == 25:
                resp.append('S')
            else:
                resp.append(casaAtual+dados)
    cobraXescada = False

for i in range(0, jogadores):
    print(resp[i])
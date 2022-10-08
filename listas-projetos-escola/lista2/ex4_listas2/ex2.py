dados = list()
par = list()
impar = list()

for x in range (0, 10):
    num = int(input(f'Digite {x+1}º números: '))
    dados.append(num)
    if dados[x] % 2 == 0:
        par.append(dados[x])
    else:
        impar.append(dados[x])

p = len(par)
for i in range(0, p-1):
    for x in range(0, p-1):
        if par[x] > par[x+1]:
            aux = par[x]
            par[x] = par[x+1]
            par[x+1] = aux
print(f'lista original:\n{dados}\npares:\n{par}\nimpares:')
i = len(impar)
for x in range(0, i-1):
    for y in range(0, i-1):
        if impar[x] > impar[x+1]:
            aux = impar[x]
            impar[x] = impar[x+1]
            impar[x+1] = aux
print(impar)


val = list()
aux = list()
valores = dict()
def calcular(*dados):
    total_area = 0
    #print(dados)
    for v in dados:
        #area = v[1][0] * v[1][1]
        #print(area)
        #print(v)
        for x in v:
            #print(x)
            area = x['medidas'][0] * x['medidas'][1]
            total_area += area
            print(f'Comodo: {x["nome"]} área = {area}')
    print(f'a soma de todas as áreas = {total_area}')


while True:
    valores['nome'] = input('Digite o nome do cômodo: ')


    comp = float(input('Digite o comprimento: '))
    larg = float(input('Digite a largura: '))
    
    while comp <= 0:
        comp = float(input('Digite um comprimento válido: '))
    while larg <= 0:
        larg = float(input('Digite uma largura válida: '))
    aux.append(comp)
    aux.append(larg)

    valores['medidas'] = aux[:]
    val.append(valores.copy())
    aux.clear()
    
    if int(input('deseja continuar? 1-sim/qualquer número-não\n')) != 1:
        break
calcular(val)
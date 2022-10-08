from operator import itemgetter
from random import randint
d = {
    'jogador1' : randint(1, 6),
    'jogador2' : randint(1, 6),
    'jogador3' : randint(1, 6),
    'jogador4' : randint(1, 6)
}

posi = list()
colocacoes = list()

print('Valores sorteados:')

#mostra os valores de dados e indices
for chave, valor in d.items():
    print(f'   O [{chave}] tirou [{valor}]')
    posi.append(valor) #recebe valores do dado
#print(posi)

#ordena a lista posi com o valores do dicionario
for x in range(0, 3):
    for i in range(0, 3):
        if posi[i] < posi[i+1]:
            aux = posi[i]
            posi[i] = posi[i+1]
            posi[i+1] = aux
#print(posi)

for x in range(0, 4):
    for chave, valor in d.items():
        #verifica se o valor de uma lista é igual ao valor do dicionario
        if posi[x] == valor:
            #se não existe o indice do dicionário dentro de uma segunda lista:
            if not chave in colocacoes: 
                colocacoes.append(chave)
                colocacoes.append(valor)
#print(colocacoes)

print('Ranking dos jogadores:')

#mostra as colocações da lista, 1º - 4º
lugares = 1
for x, i in enumerate(colocacoes):
    if x % 2 == 0:
        print(f'{lugares}º lugar ==> {colocacoes[x]} {colocacoes[x+1]} ')
        lugares += 1
    


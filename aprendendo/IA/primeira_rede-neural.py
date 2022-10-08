#perceptron 1 de uma camada
entradas = [1, 7, 5] #3 entradas e 3 pesos
pesos = [0.8, 0.1, 0]

#faz a função inicial de uma rede neural
def soma(ent, pes):
    soma = 0
    for i in range(0, 3):
        #print(f'entradas = {ent[i]} e pesos = {pes[i]} ')
        soma += ent[i] * pes[i]
    return soma

def stepFunction(soma):
    #função gráfica, mas aq n vai ser ainda
    #n precisa do else, se for verdadeiro irá executar o return 1 e n irá executar o return 0
    if soma >= 1:
        return 1
    return 0


som = soma(entradas, pesos)
#print(som)
r = stepFunction(som)
#print(r)


import numpy as np
#matriz das entradas
entradas = np.array([[0,0],[0,1], [1,0], [1,1]])
#duas entradas para dois pesos!!!
#saídas supervisionadas, q já tem resposta
#saidas = np.array([0, 0, 0, 1]) - operador lógico 'AND'
saidas = np.array([0, 1, 1, 1])# - operador 'OR'
#saidas = np.array([0, 1, 1, 0]) - operador 'XOR' - nesse caso, ele n encontra um padrão para os pesos!
pesos = np.array([0.0, 0.0])
'''en [0,0]
   pe [0.0, 0.0]
    0 * 0.0 + 0 * 0.0
    analisar alí em treinar, na passagem de parametro
'''

taxaAprendizagem = 0.1 #valor p aprender
def stepFunction(soma):
    if soma >= 1:
        return 1
    return 0

def calculaSaida(registro):
    s = registro.dot(pesos) # s += entradas[x] * pesos[x], algo assim
    return stepFunction(s)

def treinar():
    erroTotal = 1
    while erroTotal != 0:
        erroTotal = 0
        for i in range(0, len(saidas)): #para comparar os valores com os valores da saída
            saidaCalculada = calculaSaida(np.asarray(entradas[i])) #irá passar o [0,0], [0,1], etc
            #abs serve p n fazer diferença caso a saidas esteja antes ou depois de saidaCalculada
            #p n ter valor negativo, apenas 0 ou acima de 1
            erro = abs(saidas[i] - saidaCalculada) #exemp: 0 - 0 ou 1 - 0, se erro for 0, nn existe erro
            erroTotal += erro
            for j in range(0, len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                #entradas[0][0] = 0 ent[0][1] = 0, ent[2][0] = 1 ent[2][1] = 0
                #é mais fácil de entender isso com os desenhos das redes neurais!!!
                print(f'Peso{j} atualizado {pesos[j]} ')
        print(f'total de erros: {erroTotal} ')
print(f'entradas = {entradas} ')
print(f'saídas = {saidas} ')
treinar()
print('rede neural treinada!')
print(calculaSaida(entradas[0]))
print(calculaSaida(entradas[1]))
print(calculaSaida(entradas[2]))
print(calculaSaida(entradas[3]))
print(calculaSaida(np.asarray([3,2])))

'''enquanto erro != 0
para cada registro:
calcula a saída com os pesos atuais
compara a saída esperada com a saída calculada, somando o erro
para cada peso da rede
atualiza o peso:
peso = peso + (taxaAprendizagem * entrada * erro)
'''
import numpy as np
entradas = np.array([[4,3], [1,1], [2,2], [2,3], [1,2], [5,3], [3,3]])
saidas = np.array([1, 1, 0, 0, 1, 1, 0])
pesos = np.array([0.0, 0.0])

taxaAprendizado = 0.1

def stepFunction(soma):
    if soma >= 1:
        return 1
    return 0

def calcularSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

def treinar():
    totalErro = 1
    while totalErro != 0:
        totalErro = 0
        for i in range(0, len(saidas)):
            saidaCalculada = calcularSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            totalErro += erro
            for j in range(0, len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizado * entradas[i][j] * erro)
                print(f'pesos {j} = {pesos[j]} ')
        print(f'total de erros: {totalErro} ')

print(entradas)
print(saidas)
print(pesos)
#teste = np.array([-1,3])
treinar()

#x = calcularSaida(np.asarray(teste))
#print(x)
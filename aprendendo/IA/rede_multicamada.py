import numpy as np

def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

#a = np.exp(1) #numero de euler
#a = sigmoid(50)
entradas = np.array([
    [0,0], [0,1], [1,0], [1,1]
])
saidas = np.array([
    [0], [1], [1], [0]
])
#pesos0 das entradas para ocultas
pesos0 = np.array([
    [-0.424, -0.740, -0.961],
    [0.358, -0.577, -0.469]
])
#pesos1 das ocultas para saídas
pesos1 = np.array([
    [-0.017], [-0.893], [-0.148]
])
epocas = 100 #quantos loops o programa irá rodar
for j in range(epocas):
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada, pesos0) #multiplicação e somatório dos arrays
    camadaOculta = sigmoid(somaSinapse0)
    
    somaSinapse1 = np.dot(camadaOculta, pesos1)
    camadaSaida = sigmoid(somaSinapse1)
    
    erroCamadaSaida = saidas - camadaSaida
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))

#print(erroCamadaSaida)
#print(mediaAbsoluta)


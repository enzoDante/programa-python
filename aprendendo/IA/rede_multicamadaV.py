import numpy as np

def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))
#a = np.exp(1) #numero de euler
#a = sigmoid(50)

def sigmoidDerivada(sig):
    return sig * (1-sig)

#a = sigmoid(0.5)
#b = sigmoidDerivada(a)
#print(f'aaaaa: {a} eeee bbbb {b}\n\n')

entradas = np.array([
    [0,0], [0,1], [1,0], [1,1]
])
saidas = np.array([
    [0], [1], [1], [0]
])
#pesos0 das entradas para ocultas
# pesos0 = np.array([
#     [-0.424, -0.740, -0.961],
#     [0.358, -0.577, -0.469]
# ])
#pesos1 das ocultas para saídas
# pesos1 = np.array([
#     [-0.017], [-0.893], [-0.148]
# ])

pesos1 = 2 * np.random.random((3,1)) - 1
pesos0 = 2 * np.random.random((2,3)) - 1


epocas = 1000000 #quantos loops o programa irá rodar
taxaAprendizagem = 0.5
momento = 1
for j in range(epocas):
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada, pesos0) #multiplicação e somatório dos arrays
    camadaOculta = sigmoid(somaSinapse0)
    
    somaSinapse1 = np.dot(camadaOculta, pesos1)
    camadaSaida = sigmoid(somaSinapse1)
    
    erroCamadaSaida = saidas - camadaSaida
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))
    print("Erro: "+ str(mediaAbsoluta))

    derivadaSaida = sigmoidDerivada(camadaSaida)
    deltaSaida = erroCamadaSaida * derivadaSaida

    pesos1Transposta = pesos1.T
    deltaSaidaxPeso = deltaSaida.dot(pesos1Transposta)
    deltaCamadaOculta = deltaSaidaxPeso * sigmoidDerivada(camadaOculta)

    camadaOcultaTransposta = camadaOculta.T
    pesosNovo1 = camadaOcultaTransposta.dot(deltaSaida)
    pesos1 = (pesos1 * momento) + (pesosNovo1 * taxaAprendizagem)

    camadaEntradaTransposta = camadaEntrada.T
    pesosNovo0 = camadaEntradaTransposta.dot(deltaCamadaOculta)
    pesos0 = (pesos0 * momento) + (pesosNovo0 * taxaAprendizagem)



#print(deltaSaidaxPeso)

#print(erroCamadaSaida)
#print(mediaAbsoluta)


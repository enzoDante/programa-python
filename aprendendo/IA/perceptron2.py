#para melhorar os processamentos, se utiliza o numpy
#uso científico muito usado com redes neurais
import numpy as qualquer_coisaq

#criando vetor com o numpy
entradas = qualquer_coisaq.array([1, 7, 5])
pesos = qualquer_coisaq.array([0.8, 0.1, 0])

def soma(ent, pes):
    return ent.dot(pes)
    #.dot ja faz a multiplicação e a soma

def stepFunction(soma):
    if soma >= 1:
        return 1
    return 0

som = soma(entradas, pesos)
print(som)
r = stepFunction(som)
print(r)
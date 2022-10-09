import random
import matplotlib.pyplot as plt

cores = ['#FF1B16', '#FF1B16', '#0FB839', '#0FB839']
numeros = list()
nums = list()
quantidade = list()
for i in range(0, 1001):
    numeros.append(random.randint(0, 10) + random.randint(0, 10))

for i in range(0, 21):
    nums.append(i)
    quantidade.append(numeros.count(i))

print(numeros)
print("="*30)
print(quantidade)
plt.rcParams['figure.figsize'] = [12, 8] #tamanho da figura
plt.bar(nums, quantidade, color=cores)

plt.xticks(nums) #define os nomes de cada coluna no eixo x
plt.xlabel('Números de 0 a 20')
plt.ylabel("Total de vezes que esse número apareceu")
plt.title("Número aleatórios")
plt.show()
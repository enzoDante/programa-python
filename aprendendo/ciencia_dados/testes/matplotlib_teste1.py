import random
import matplotlib.pyplot as plt

numeros = list()
nums = list()
quantidade = list()
for i in range(0, 501):
    numeros.append(random.randint(0, 10) + random.randint(0, 10))

for i in range(0, 21):
    nums.append(i)
    quantidade.append(numeros.count(i))

print(numeros)
print("="*30)
print(quantidade)
plt.bar(nums, quantidade, color='green')
plt.xticks(nums) #define os nomes de cada coluna no eixo x
plt.xlabel('Números de 0 a 200')
plt.ylabel("Total de vezes que esse número apareceu")
plt.title("Número aleatórios")
plt.show()
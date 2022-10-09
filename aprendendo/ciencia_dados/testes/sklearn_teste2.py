from sklearn import datasets
import matplotlib.pyplot as plt #gerar gráficos

iris = datasets.load_iris()
features = iris.data #cada coluna é uma caracterisitca
#features = iris['data'] mesma coisa acima
#print(features) 
#features = iris.data[: , [0,1,2,3]] --escolhe as colunas q desejo
target = iris.target

#target.shape#150 valores (0,1 e 2)
#x = target.reshape(target.shape[0], -1)#cria uma lista p cada valor [[0],[0],[0],...,[2],]
#print(target)# 0000 1111 2222
print('==='*30)
#=======================================================================
featureAll = list()
for obs in features:
    featureAll.append([obs[0] + obs[1] + obs[2] + obs[3]])#somando os campos
print(featureAll)

#alpha de 0 a 1 é opacidade dele
plt.scatter(featureAll, target, color='red', alpha=1.0)
plt.rcParams['figure.figsize'] = [10, 8] #tamanho da figura
plt.title('Dados de iris título')#titulo do gráfico
plt.xlabel('Featurrress') #nome de x e y do gráfico
plt.ylabel('targeeetttss')
plt.show()
#em targeeetttss 0-setosas 1.. 2...
#=======================================================================
#agr gerar um gráfico com relação ao comprimento etc da sépalas
sepal_len = list()
sepla_width = list()
#print(iris.feature_names)#nome das colunas (recursos)
#['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
for i in features:
    sepal_len.append(i[0]) #comprimento da sépala
    sepla_width.append(i[1])#largura da sépala
groups = ('Iris setosa', 'Iris versicolor', 'iris virginica') #tupla dos tipos de sépalas
colors = ('blue', 'green', 'red')
data = ((sepal_len[:50], sepla_width[:50]), (sepal_len[50:100], sepla_width[50:100]), (sepal_len[100:150], sepla_width[100:150]))
#é tridimensional!! (([valores], [valores2]), ([v], [v2]),...,([v],[v2]))

#zip percorre paralelamente os valores
#OBS:todos elementos tem 0 á 2 indices! data= (),(),() colors= '', '', '' groups= '' '' ''
for item, cor, group in zip(data, colors, groups):
    #item = (sepal_len[:50], sepal_width[:50]),(sepal_len[50:100], sepal_width[50:100]),...
    x0, y0 = item #x recebe primeira lista e y recebe segunda lista
    #x = item[0] e y = item[1]
    print(item)#([coluna0],[coluna1])
    print("=--"*30)

    plt.scatter(x0, y0, color=cor, alpha=1)
plt.title('iris dados deles largura e comprimento')
plt.xlabel('sepala comprimento')
plt.ylabel('sepala largura')
plt.show()
#=======================================================================
#agora um gráfico de comprimento e largura da pétala
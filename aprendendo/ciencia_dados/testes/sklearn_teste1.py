from sklearn import datasets
iris = datasets.load_iris()
print(iris.data) #cada linha é uma amostra, cada coluna é um recurso

print(iris.feature_names)#nome das colunas (recursos)
print("="*30)
#list(iris.target_names)
print(iris.target_names)
print("="*30)
print(iris.target)#espécies diferente (0, 1 e 2)

x = iris.data #armazena recursos(feature)
y = iris.target #armazena resposta
print("==="*35)
print(x)
print("==="*35)
print(y)
#distancia entre dois pontos na diagonal = raiz de (xb-xa)²+(yb-ya)²
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd

iris = datasets.load_iris()
irs = pd.DataFrame(iris.data, columns=iris['feature_names'])
irs['class'] = iris.target
print(irs)
print('='*20)
print(irs.head())#mostra as 5 primeiras linhas, caso queira mais linhas, passe ela como parametro
print(irs.columns)#mostra todas as colunas
print(irs.count())#total de linhas

print(irs.describe())#desvio, média, min, max, etc
#====================NearestNeighbours=============
#dividir os valores(x-sepal lenght, sepal width, petal lenght e petal width)
#(y-rótulos classes[0, 1 e 2])
x = irs.iloc[:, :-1].values#exclui a última coluna
y = irs.iloc[:, 4].values#somenta a última coluna
print(x)
print(y)
#treinamento e teste
#80% dados de treino e 20% de dados de teste ou seja
#150 registros-120 p treinar e 30 p testar
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)
# print(x_train)#somente separou os dados!!!
# print('='*20)
# print(x_test)
#deve ter normalização!! (dados na mesma escala)
#preprocessing do sklearn - pode padronizar com StandardScaler()
#ignora a distribuição e transforma os dados p forma com média próxima de 0 e de 1
#distribuição normal chamada de distribuição de Gauss/Gaussiana
scaler = StandardScaler()
scaler.fit(x_train)#média e desvio da distribuição p padronizar os dados
x_train = scaler.transform(x_train)#aplica os cálculos p fazer a transformação nos dados
x_test = scaler.transform(x_test)
print(x_train)
print('='*20)
print(x_test)
#====================================treinar e prever===========================
#https://www.codigofluente.com.br/aula-06-scikit-learn-vizinhos-mais-proximos-knn/
classifier = KNeighborsClassifier(n_neighbors=5)#valor do raio do exemp da img
#5 é um bom valor p começar, é mais comum no algoritmo KNN
classifier.fit(x_train, y_train)#treinar o algoritmo

#agr fazer previsões dos dados de teste
y_pred = classifier.predict(x_test)
#p avaliar um algoritmo usa(matriz de confusão, precisão, recall e pontuação f1) métricas
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
#o algoritmo classificou os 30 registro de teste com quase 100% de precisão

classifier = KNeighborsClassifier(n_neighbors=9)
classifier.fit(x_train, y_train)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

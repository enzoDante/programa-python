from sklearn import datasets
import numpy as np
import pandas as pd

iris = datasets.load_iris()
#dataframe usando numpy array
df_iris = pd.DataFrame(np.column_stack((iris.data, iris.target)), columns=iris.feature_names + ['target'])
# print(iris.data)
# print('=-'*20)
# print(iris.target)
# print('=-'*20)
# print(iris.feature_names)
print(df_iris)
print("=-="*31)
print(df_iris.describe())
#do comando describe (count, mean, std, min, 25%,50%,75% e max) para cada coluna!!!
#mean = média, std=desvio padrão, min-max=valores minimos e maximos, 25,50,75-porcentis
#q dividem a amostra por ordem crescento dos dados

#========================================================================================
#teste com dataframe
# t = [['x', 'y', 'z', 'a', ''],
# ['x', 'y', '', 'a', 'b'],
# ['x', 'y', 'z', 'a', 'b'],
# ['x', 'y', 'z', '', 'b'],
# ['x', '', 'z', 'a', ''],
# ['', 'y', '', 'a', 'b']]
# y = [1,2,0,4, 0, 6]
# df_teste = pd.DataFrame(np.column_stack((t, y)), columns=['teste']+['2']+['3']+['4']+['5']+['6'])
# print(df_teste)
#em columns= é obrigatório ter todas as colunas!! caso for usar esse comando! nesse caso, não pode ter menos de 6 nomes de colunas ou mais
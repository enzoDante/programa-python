import pandas as pd
import numpy as np
#criar array numpyy
data = np.array(['a','b','c','d'])
#gerar objeto series do pandas
s1 = pd.Series(data) #series é unidimensional!!!
print(s1)

data2 = np.array(['a','b','c','d'])
s2 = pd.Series(data2, index=[60,61,62,63])
print(s2)

data3 = {'a':0., 'b':1., 'c': 2.}
s3 = pd.Series(data3)
print(s3)

data4 = {'a':0., 'b':1., 'c':2.}
s4 = pd.Series(data4, index=['b','c','d','a'])
print(s4)

s = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(s['a'])
print(s[['a','c','d']])
#print(s['f'])#n existe erro

#dataframe bidimensional!!!=============================================
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)

data = [['Maria', 10], ['Carlos', 12], ['Paulo', 13]]
df = pd.DataFrame(data, columns=['Nome', 'Idade'])
print(df)

#df = pd.DataFrame(data, columns=['Nome', 'Idade'], dtype=float)
#print(df)
data = {'Nome':['Marcos', 'Paula', 'Lia', 'Carlos'], 'Idade':[28, 34, 29, 42]}
df = pd.DataFrame(data)
print(df)

data = {'Nome': ['Marcos', 'Paula', 'Lia', 'Carlos'], 'Pontuação': [7.5, 6.8, 5.9, 8.3]}
df = pd.DataFrame(data, index=['Rank1', 'Rank2', 'Rank3', 'Rank4'])
print(df)

data = [{'a': 1, 'b': 2}, {'a':5, 'b':10, 'c':20}]
df = pd.DataFrame(data)
print(df)
df = pd.DataFrame(data, index=['primeiro', 'segundo'])
print(df)
#valor das colunas deve ser iguais as chaves de dicionario!!!
df1 = pd.DataFrame(data, index=['primeiro', 'segundo'], columns=['a', 'b'])
df2 = pd.DataFrame(data, index=['primeiro', 'segundo'], columns=['a', 'b1'])
print(df1)
print(df2)

dic = {'um': pd.Series([1,2,3], index=['a','b','c']),
'dois': pd.Series([1,2,3,4], index=['a','b','c','d'])}
df = pd.DataFrame(dic)
print(df)
print(df['um'])
#adicionando coluna
df['três'] = pd.Series([10,20,30], index=['a','b','c'])
print(df)
df['quatro'] = df['um'] + df['três']
print(df)
#apagar dados!-----
d = {'um': pd.Series([1,2,3], index=['a','b','c']),
'dois': pd.Series([1,2,3,4], index=['a','b','c','d']),
'três': pd.Series([10,20,30], index=['a','b','c'])}
df = pd.DataFrame(d)
print(df)
del df['um'] #usando del
print(df)
df.pop('dois') #usando pop
print(df)

dic = {'um': pd.Series([1,2,3], index=['a','b','c']),
'dois': pd.Series([1,2,3,4], index=['a','b','c','d'])}
df = pd.DataFrame(dic)
print(df.loc['b'])#mostra somente os valores da coluna 'b'
print(df.iloc[2])#mostra somente o indice 2
print(df[2:4])#mostra indice 2 á 3

a = [[1,2], [3,4], [5,6], [7,8]]
df = pd.DataFrame(a, columns=['a', 'b'])
#df2 = pd.DataFrame([[5,6], [7,8]], columns=['a','b'])
# df = df.append(df2) - esse comando será removido!!!
print(df)
df = df.drop(0)#deleta as linha com rótulo 0
print(df)#ou seja, deleta a linha determinada

#==============[FIM]============
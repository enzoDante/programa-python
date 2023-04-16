import numpy as np
import pandas as pd
import plotly.express as px

#x = np.array([1, 2, 3, 4, 5])
#x = np.array([[1, 2, 3], [4, 5, 6]])
x = np.random.randint(50, size=(2, 3))
#size=(linhas, colunas)

#colunas = ['x', 'y', 'z']
y = pd.DataFrame(x, columns = ['x', 'y', 'z'])

print(x)
print('aaa')
print(y)
print('separa\n')

numpyArray = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)], dtype=[("a", "i4"), ("b", "i4"), ("c", "i4")])
dataf = pd.DataFrame(numpyArray)
print(dataf)

#===============================
fig = px.scatter_3d(y, x='x', y='y', z='z')
fig.show()
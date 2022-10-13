from turtle import color
import pandas as pd
import pymongo
import matplotlib.pyplot as plt

#salvar como: Pasta de Trabalho do Excel
#caso não faça isso, não será possível ler o arquivo!

#conexao com o banco de dados
cliente = pymongo.MongoClient("mongodb://localhost:27017/")
meu_banco = cliente['banco_de_dados']

colecao = meu_banco['projeto4b']

df = pd.read_excel(r"D:/codigo-vsCode/programa-python/banco-de-dados/projeto_bd_4/ccont_2t_AC_271020181441.xlsx", sheet_name='ccont_2t_AC_271020181441')

secoes = df.shape[0]
totalm = 0
atual = ''
#para gerar gráficos:
municipios = list()
nr_zona = list()

for i in range(len(df)):
    if(atual != df.loc[i, 'NM_MUNICIPIO']):
        totalm += 1
        atual = df.loc[i, 'NM_MUNICIPIO']
        municipios.append(df.loc[i, 'NM_MUNICIPIO'])
        nr_zona.append(df.loc[i, 'NR_ZONA'])
#print(totalm)

colec = colecao.find().sort('_id')
id = 0
for i in colec:
    id = i['_id']
id += 1


valor = {'_id': id, 'Seções':secoes, 'Municipios': totalm}
colecao.insert_one(valor)

#x (horizontal) nomes de municipios
#y (vertical) zona valores numéricos
cores = ['#0D3A52', '#19709E', '#2194D1', '#57B6EB']
#gerar o gráfico
plt.rcParams['figure.figsize'] = [12, 8]
plt.grid(b=True, linestyle=':', which='major', color='#9BD6E0')#grey #63EBE1 #9BD6E0
plt.barh(municipios, nr_zona, color=cores)
plt.xticks(nr_zona)

plt.ylabel("Municípios")
plt.xlabel("NR_Zonas")
plt.title("Municípios x Zonas")
plt.show()
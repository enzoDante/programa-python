import pandas as pd
import openpyxl

p = pd.read_excel(r'D:/codigo-vsCode/programa-python/listas-projetos-escola/lista4/teste/testarxml.xlsx', sheet_name='Plan1')
print(p)
#r ante do caminho: indica q faremos leitura
#mostra quantidade de dados em linhas
print(f'Linhas com dados usando len {len(p)} ou shape {p.shape[0]} ')
#agr msm coisa mas p saber as colunas
print(f'Quantas colunas usando len: {len(p.columns)} ou com shape: {p.shape[1]} ')

#mostrando apenas alguns dados
print(p[['nome', 'media']])#ou
print(f'{p.media}')
#calculos das colunas
p['soma das notas'] = p['notas'] + p['notas2']
print(p)

#linha especifica da planilha   linha de indice 2 até ultima linha
print(p[2:len(p)])
#limitando os dados a ser mostrado -- vai do indice 0 até 2 [0:3]
print(p['nome'][0:3])

#outra forma de mostrar colunas
for i, x in enumerate(p['notas']):
    print(f'linha: {i}= nota {x} ')
#limita quais colunas vai usar
#p = pd.read_excel(r'caminho/nsei.xlsx', sheet_name='Planilha1', usecols=['nome','notas','notas2'])

#loc -- busca dados especificos na planilha
print(p.loc[0:4])
#também pode indicar intervalos de linhas e colunas
print(p.loc[2:5, 'nome':'notas2'])
#iloc
print(p.iloc[2:9])
#mostra linha 2 a 4 --- e coluna 2 a 3
print(p.iloc[2:5, 2:4])
#mostra linha 3 e 5, e colunas 2 ate 3
print(p.iloc[[3, 5], 2:4])
#mostra linha 3 coluna 1 -- note nesse caso usa a vírgula e nn ':'
print(p.iloc[3,1])


#alterando dados do dataframe (ele n altera do arquivo original!)
p.loc[p['nome']=='Aa', 'notas'] = 7
print(p)



#outra forma de ver as planilhas, porém, é possível ver mais de uma!
#criando dataframe p representar o arquivo testarxml.xlsx
df = pd.ExcelFile('D:/codigo-vsCode/programa-python/listas-projetos-escola/lista4/teste/testarxml.xlsx')
#mostra todas as planilhas do arquivo
print(f'Planilhas do arquivo ==>> {df.sheet_names} ')

#parse - especifica uma planilha
aba1 = df.parse('Plan1')
aba2 = df.parse('Planilha1')
print(aba1)
print('=======')
print(aba2)
#alterar dados do arquivo original:
#df.to_excel('caminhonomearquivo', sheet_name = 'nomeplanilha', na_rep = '#N/A', header = True, index = False)
#to_excel = gera uma tabela excel do dataframe
#sheet_name = nome da planilha q será criada
#na_rep '#N/A' - caso exista células vazias. irá inserir 'NaN' nas vazias
#header 'true' - titulos serão o mesmo do dataframe já criado
#index 'false' - nn gerar a tabela com os índices do dataframe

import pandas as pd
import openpyxl

dicionario = {'Carros': ['A', 'B', 'C', 'D'],
            'Ano':[2015, 2019, 2021, 2022],
            'valores':[50000.00, 60000.0, 100000.0, 2000000.09]
            }
print(dicionario)
#criando um dataframe
df = pd.DataFrame(dicionario)
print(df)

#gerando o arquivo com esses dados
df.to_excel('D:/codigo-vsCode/programa-python/listas-projetos-escola/lista4/teste/carros.xlsx', sheet_name='Planilha1', na_rep='#N/A', header=True, index=False)

df1 = pd.DataFrame({'Data':[2,4,6,8]})
df2 = pd.DataFrame({'Data':[100,150,200,250]})
df3 = pd.DataFrame({'Data':[3,6,9,12]})
#usando excelWriter p criar arquivo usando engine openpyxl
arquivo = pd.ExcelWriter('tabelasexemp.xlsx', engine='openpyxl')

df1.to_excel(arquivo, sheet_name='Tabela 1', index=False)
df2.to_excel(arquivo, sheet_name='Tabela 2', index=False)
df3.to_excel(arquivo, sheet_name='Tabela 3', index=False)
#fecha o excelWriter e gera o arquivo
arquivo.save()
#isso de salvar será removido futuramente!!!
#==============openpyxl==================================
#workbook - cria planilha excel
#load_workbook - carrega planilha existente
#OBS: openpyxl trata o excel exatamente como planilha, ent as linha e colunas são iguais

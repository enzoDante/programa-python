#Projeto POOI 4 bimestre
#Enzo Dante, Samuel Pascoal e Bruno Braga
import mysql.connector
import pandas as pd
import openpyxl
#==============abrir o banco de dados==========
def abrirbanco():
    try:
        global conn
        conn = mysql.connector.Connect(
            host='localhost',
            database='univap',
            user='root',
            password=''
        )
        if conn.is_connected():
            global sql 
            sql = conn.cursor()
            return 1
        else:
            print('não foi possível conectar ao banco')
            return 0
    except:
        print(f'Ocorreu um erro na conexão do banco de dados!')
#verificar se existe o registro
def verificarprof(c=0):
    try:
        sql = conn.cursor()
        sql.execute(f'select * from professores where registro={c};')
        tabela = sql.fetchall()
        
        if sql.rowcount > 0:
            for i in tabela:
                print(f'Professor: {i[1]}')
            return True
        else:
            return False
    except:
        print("não foi possível buscar pelo professor!")
        return False

#============main===================
if abrirbanco() == 1:
    while True:
        try:
            codigo = int(input("Digite o código de um professor: "))
            if verificarprof(codigo) != True:
                print('Professor inexistente!')
                continue #--- caso não exista o código
            break
        except:
            print("Digite um valor numérico!")
    print("boa")

    dici = {'Carros': ['A', 'B', 'C', 'D'],
            'Ano':[2015, 2019, 2021, 2022],
            'valores':[50000.00, 60000.0, 100000.0, 2000000.09]}
    df = pd.DataFrame(dici)

    dici = {'Carros': ['E', 'F', 'G', 'H'],
            'Ano':[2015, 2019, 2021, 2022],
            'valores':[50000.00, 60000.0, 100000.0, 2000000.09]}
    df2 = pd.DataFrame(dici)

    arquivo = pd.ExcelWriter('D:/codigo-vsCode/programa-python/listas-projetos-escola/projetos/carross.xlsx', engine='openpyxl')
    #df.to_excel('D:/codigo-vsCode/programa-python/listas-projetos-escola/projetos/carross.xlsx', sheet_name='Planilha1', na_rep='#N/A', header=True, index=False)
    df.to_excel(arquivo, sheet_name='planilha1', index = False)
    df2.to_excel(arquivo, sheet_name='planilha2', index = False)
    arquivo.save()
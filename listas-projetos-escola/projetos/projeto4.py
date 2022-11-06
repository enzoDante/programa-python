#Projeto POOI 4 bimestre
#Enzo Dante, Samuel Pascoal e Bruno Braga
import mysql.connector
import pandas as pd
import openpyxl
#================================abrir o banco de dados========================
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
#================================verificar se existe o registro============
def verificarprof(c=0):
    try:
        sql = conn.cursor()
        sql.execute(f'select * from professores where registro={c};')
        tabela = sql.fetchall()
        global nomeprof
        
        if sql.rowcount > 0:
            for i in tabela:
                nomeprof = i[1]
                print(f'Professor: {i[1]}')
            return True
        else:
            return False
    except:
        print("não foi possível buscar pelo professor!")
        return False
#==================================dados de determinado professor===================
def profd(c):
    try:
        sql = conn.cursor()
        sql.execute(f'select * from disciplinasxprofessores inner join disciplinas on (codigodisc=coddisciplina) where codprofessor={c} and anoletivo=2021')
        #inner join professores on (registro=codprofessor) where registro={c}
        tabela = sql.fetchall()
        if sql.rowcount > 0:
            nome_disciplinac = ''
            dadoprofd = list()
            for i in tabela:
                nome_disciplinac = f'{i[7]} código: {i[1]}'
                #, 'codigo disciplina': i[1], 'nome disciplina': i[7]
                linha = {'codigo': int(i[0]), 'curso': int(i[3]), 'carga horaria': i[4]}
                dadoprofd.append(linha)

            df = pd.DataFrame(dadoprofd)
            total_horas = 0
            for i in df['carga horaria']:
                total_horas += i
                
            df.loc['total de horas'] = '-'
            df.loc['total de horas', 'carga horaria'] = total_horas

            df.loc['Professor'] = '-'
            df.loc['Professor', 'codigo'] = f'{nomeprof} - ano letivo: 2021'

            df.loc['Disciplina'] = '-'
            df.loc['Disciplina', 'codigo'] = f'{nome_disciplinac}'
            #print(df)
            return df
        return False

    except:
        print('ocorreu um erro ao buscar por dados do professor!')
        return False

#==================================digitar codigo prof======================
def digitCodigo():
    while True:
        try:
            global codigo
            codigo = int(input("Digite o código de um professor: "))
            if verificarprof(codigo) != True:
                print('Professor inexistente!')
                continue #--- caso não exista o código
            break
        except:
            print("Digite um valor numérico!")
#==================professores por cursos==============
def profxcurso():
    try:
        sql = conn.cursor()
        sql.execute(f'select nomeprof, curso from professores inner join disciplinasxprofessores on (registro=codprofessor) where anoletivo=2021')
        tabela = sql.fetchall()
        if sql.rowcount > 0:
            print('\n\n')
            #print(tabela)
            tt = list()
            for i in tabela:
                #print(i)
                #print(i[0])
                t = {f'Curso {i[1]}': i[0]}
                tt.append(t)

            print(tt)
            for i in tt:
                print(i)


            df = pd.DataFrame(tt)
            print(df)


    except:
        print("Ocorreu um erro ao buscar por dados do banco de dados!")

#================================================main======================
if abrirbanco() == 1:
    #======parte 1===========
    digitCodigo()

    while True:     
        dados = profd(codigo)
        try:
            if(dados == False):
                print('Esse professor não tem dados no ano letivo de 2021')
                digitCodigo()
                
        except:
            print('\n\n')
            print(dados)
            break
    #=======parte 2==========
    profxcurso()





    # dici = {'Carros': ['A', 'B', 'C', 'D'],
    #         'Ano':[2015, 2019, 2021, 2022],
    #         'valores':[50000.00, 60000.0, 100000.0, 2000000.09]}
    # df = pd.DataFrame(dici)

    # dici = {'Carros': ['E', 'F', 'G', 'H'],
    #         'Ano':[2015, 2019, 2021, 2022],
    #         'valores':[50000.00, 60000.0, 100000.0, 2000000.09]}
    # df2 = pd.DataFrame(dici)

    # arquivo = pd.ExcelWriter('D:/codigo-vsCode/programa-python/listas-projetos-escola/projetos/dadosdp.xlsx', engine='openpyxl')

    #df.to_excel('D:/codigo-vsCode/programa-python/listas-projetos-escola/projetos/carross.xlsx', sheet_name='Planilha1', na_rep='#N/A', header=True, index=False) - nn da


    # dados.to_excel(arquivo, sheet_name='planilha1', index = True)
    # df2.to_excel(arquivo, sheet_name='planilha2', index = False)
    # arquivo.save()
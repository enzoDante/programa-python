from time import sleep
import mysql.connector

lista = list()
dicio = dict()

disciplinas_por_curso = list()

def banco():
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
    except Exception as erro:
        print(f'erro: {erro}')
#=====buscar por disciplinas de determinada relação==========
def disciplinas(c=0, curso=0):
    try:
        sql = conn.cursor()
        sql.execute(f'select * from disciplinas where codigodisc={c}')
        discs = sql.fetchall()
        if sql.rowcount > 0:
            
            for d in discs:
                cod_disc = d[0]
                nome_disc = d[1]

                disciplinas_por_curso.append(f'{curso} {cod_disc} | {nome_disc}')
    except:
        print("Ocorreu um erro ao buscar dados na tabela disciplinas!\n")


#==========buscar por dados de determinado professor======
def disciplinasxprofs(prof=0):
    try:
        
        sql = conn.cursor()
        sql.execute(f'select * from disciplinasxprofessores where codprofessor={prof} order by curso')
        discprofs = sql.fetchall()
        if sql.rowcount > 0:
            
            for dados in discprofs:
                disciplinas(dados[1], dados[3])

                dicio['curso'] = disciplinas_por_curso.copy()

            disciplinas_por_curso.clear()

            lista.append(dicio.copy())
            dicio.clear()

                
    except:
        print("Ocorreu um erro ao buscar pela relação do professor com disciplinas!\n")

#=========buscar por professor=======
def professores():
    try:
        sql = conn.cursor()
        sql.execute('select * from professores;')
        tabela = sql.fetchall()
        if sql.rowcount > 0:
            for i in tabela:
                professor = i[0]

                global arquivo 
                arquivo = open(f'D:/codigo-vsCode/programa-python/listas-projetos-escola/lista4/ex1_Desafios_arquivos_texto/para_b/{professor}.html', 'w')

                nome_prof = i[1]
                dicio['id_prof'] = professor
                dicio['nome_prof'] = nome_prof
                #print(dicio)                
                disciplinasxprofs(professor)
                
                format_html = f'''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{professor}</title>
</head>
<body>
    <header><h1>Disciplinas do professor: {nome_prof}</h1></header>
    <main>
        <h2>CÓDIGO DA DISCIPLINA | NOME DISCIPLINA</h2>
        
        '''
                '''print('=========')
                for i in lista:
                    print(i)'''

                for i in lista:
                    for indice, valores in i.items():
                        v = '0'
                        if indice == 'curso':
                            for lista_cursos in valores:
                                curso = f'{lista_cursos[0]}{lista_cursos[1]}'
                                if curso != v:
                                    format_html += f'''<h3>Curso: {lista_cursos[0]}{lista_cursos[1]}</h3>'''
                                    #print(f'Curso: {lista_cursos[0]}{lista_cursos[1]}')
                                    v = curso
                                format_html += f'''<p>{lista_cursos[2:]}</p>'''
                format_html +='''</main></body></html>'''
                lista.clear()
                arquivo.write(format_html)
                arquivo.close()

        else:
            print('Não existe professor cadastrado!\n')

    except:
        print('Ocorreu um erro ao procurar por determinado professor ou gerar o arquivo desse professor!')


#=========main ===========
if banco() == 1:
    if input('Deseja criar os arquivos? 1-sim qualquer tecla-não\n') == '1':
        print('Verificando dados do banco...\n')
        professores()
        print("criando arquivos...\n")
        sleep(2)
        print("arquivos criados com sucesso\n")

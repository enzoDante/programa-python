import mysql.connector
from reportlab.pdfgen import canvas
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
#=====gerar pdf===========
def gerarpdf(nome):
    pdf = canvas.Canvas(f'{nome}.pdf')



#========opcao 1============
def registroprof():
    try:
        registro = int(input("Digite um registro: "))
        while registro < 0:
            registro = int(input("Digite um registro: "))

        sql = conn.cursor()
        sql.execute(f"select * from professores where registro={registro}")

        pdf.setFillColor('black')
        pdf.setTitle('Dados de Professor')
        pdf.setFont("Helvetica-Oblique", 20)
        pdf.drawString(250, 800, 'Professor')

        pdf.setFont("Helvetica-Oblique", 15)
        profs = sql.fetchall()
        x = 700 #mm
        if sql.rowcount > 0:
            for i in profs:
                pdf.drawString(35, x, f"Nome: {i[1]} telefone: {i[2]} idade: {i[3]} Salário: {i[4]}")
                x -= 15
            
        else:
            print("Não existe esse registro")
        
    except:
        print("O registro informado não é um número ou ocorre um erro ao procurar pelo professor")
#===========opcao 2============
def caractereprof():
    try:
        #WHERE nome_p LIKE '%$valor%'
        caractere = input("Digite um caractere: ")
        while caractere == '':
            caractere = input("Digite um caractere corretamente: ")

        sql = conn.cursor()
        sql.execute(f"select * from professores where nomeprof like '%{caractere}%'")

        pdf.setFillColor('black')
        pdf.setTitle('Dados de Professor')
        pdf.setFont("Helvetica-Oblique", 20)
        pdf.drawString(250, 800, 'Professor')

        pdf.setFont("Helvetica-Oblique", 15)
        dados = sql.fetchall()
        x = 700
        if sql.rowcount > 0:
            for i in dados:
                pdf.drawString(25, x, f"Nome: {i[1]} telefone: {i[2]} idade: {i[3]} Salário: {i[4]}")
                x -= 30
    except:
        print("Erro, não foi possível achar esse professor")
#============= opcao 3====================
def cursodisc():
    try:
        c = int(input("Informe o número de um curso: "))
        sql = conn.cursor()
        sql.execute(f"select coddisciplina, nomedisc from disciplinas, disciplinasxprofessores where codigodisc=coddisciplina and curso={c}")

        pdf.setFillColor('black')
        pdf.setTitle('Disciplinas de curso')
        pdf.setFont("Helvetica-Oblique", 20)
        pdf.drawString(210, 800, 'Disciplinas de curso')

        pdf.setFont("Helvetica-Oblique", 15)
        dis = sql.fetchall()
        x = 700
        if sql.rowcount > 0:
            for i in dis:
                pdf.drawString(20, x, f"Disciplina: {i[1]}")
                x -= 30
        else:
           pdf.drawString(20, 700, f"Disciplina inexistente") 
    except:
        print("Ocorreu um erro ao procurar por disciplinas")
#========opcao 4===============
def cursoprofs():
    try:
        c = int(input("Informe o numero de um curso: "))
        sql = conn.cursor()
        sql.execute(f"select nomeprof, registro, codprofessor from professores, disciplinasxprofessores where curso={c} and codprofessor=registro")
        nomes = sql.fetchall()
        pdf.setFillColor('black')
        pdf.setTitle('professores de curso')
        pdf.setFont("Helvetica-Oblique", 20)
        pdf.drawString(210, 800, 'professores de curso')

        pdf.setFont("Helvetica-Oblique", 15)
        x = 700
        if sql.rowcount > 0:
            for i in nomes:
                pdf.drawString(20, x, f"Nome: {i[0]} ")
                x -= 30

    except:
        print("Ocorreu um erro ao procurar por professor")
#=====opcao 5==========
def cargaletiva():
    try:
        c = int(input("Informe o numero de um curso: "))
        sql = conn.cursor()
        sql.execute(f"select sum(cargahoraria),anoletivo from disciplinasxprofessores where curso={c} group by anoletivo")
        x = 700
        dados = sql.fetchall()

        pdf.setFillColor('black')
        pdf.setTitle('Carga total por ano letivo')
        pdf.setFont("Helvetica-Oblique", 20)
        pdf.drawString(150, 800, 'Carga total por ano letivo')

        pdf.setFont("Helvetica-Oblique", 15)
        if sql.rowcount > 0:
            for i in dados:
                pdf.drawString(20, x, f"Ano letivo: {i[1]}-- Carga horária total: {i[0]} ")
                x -= 30

    except:
        print("Ocorreu um erro ao procurar por carga horária")

#-====main=====-
if banco() == 1:
    while True:
        try:
            print("="*30)
            print("[1] - Dados de professor por meio de seu registro\n")
            print("[2] - Dados de professor por meio de uma inicial de nome(somente uma letra)\n")
            print("[3] - Nomes de disciplinas por meio de um curso\n")
            print("[4] - Nomes de professores por meio de um curso\n")
            print("[5] - Carga horária total de um curso meio de um ano letivo\n")
            escolha = int(input('Escolha uma opção:  '))
            while escolha < 1 or escolha > 5:
                escolha = int(input('Escolha uma opção corretamente:  '))
            
            
            nomearquivo = input("Digite um nome para o pdf: ")
            pdf = canvas.Canvas(f'D:/codigo-vsCode/programa-python/listas-projetos-escola/lista4/ex2_39_2-Desafios/{nomearquivo}.pdf')

            if escolha == 1:
                registroprof()
            elif escolha == 2:
                caractereprof()
            elif escolha == 3:
                cursodisc()
            elif escolha == 4:
                cursoprofs()
            else:
                cargaletiva()

            pdf.save()
            print(f'{nomearquivo} foi criado ')

        except:
            print("Digite um número!!!\n")
            continue
#Projeto POOI 3 bimestre
#Enzo Dante, Samuel Pascoal e Bruno Braga
import mysql.connector
from prettytable import PrettyTable
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
    except Exception as erro:
        print(f'Erro: {erro} ')
#=======================DISCIPLINAS===================
def mostrartodasDisciplinas():
    grid = PrettyTable(['Códigos das Disciplinas', "Nomes de Disciplinas"])
    try:
        comandosql = conn.cursor()
        comandosql.execute('select * from disciplinas;')
        tabela = comandosql.fetchall()
        if comandosql.rowcount > 0:
            for registro in tabela:
                grid.add_row([registro[0], registro[1]])
            print(grid)
        else:
            print('não existe disciplinas cadastradas!!!')
    except Exception as erro:
        print(f' deu erro: {erro} ')
#----------------------------------------
def consultardisciplina(cd=0):
    try:
        comandosql = conn.cursor()
        comandosql.execute(f'select * from disciplinas where codigodisc = {cd};')
        tabela = comandosql.fetchall()

        if comandosql.rowcount > 0:
            for registro in tabela:
                print(f'Nome da disciplina: {registro[1]} ')
            return 'c'
        else:
            return 'nc'
    except Exception as erro:
        return (f'deu erro: {erro} ')
#--------------------------------------------
def cadastrardisciplina(cd=0, nd=''):
    try:
        comandosql = conn.cursor()
        comandosql.execute(f'insert into disciplinas(codigodisc, nomedisc) values({cd}, "{nd}");')
        conn.commit()
        return 'Cadastro realizado'
    except Exception as erro:
        print(f'Erro> {erro} ')
        return 'não foi possível cadastrar'
#-----------------------------------------------------
def alterardisciplina(cd=0, nomedisciplina=''):
    try:
        comandosql = conn.cursor()
        comandosql.execute(f'Update disciplinas SET nomedisc="{nomedisciplina}" where codigodisc={cd};')
        conn.commit()
        return 'Disciplina atualizada!'
    except Exception as erro:
        print(f'Erro: {erro} ')
        return 'erro, não foi possível atualizar'
#-------------------------------------------------------
def excluirdisciplina(cd=0):
    try:
        comandosql = conn.cursor()
        comandosql.execute(f'delete from disciplinas where codigodisc={cd};')
        conn.commit()
        return 'deletado'
    except Exception as erro:
        print(f'Erro {erro} ')
        return 'Não foi possível deletar'
#---------------------------------------------------------
    
#=======================PROFESSORES===================
def mostrartodosProfessores():
    grid = PrettyTable(['Registro', 'Nome', 'telefone', 'idade', 'salario'])
    try:
        sql = conn.cursor()
        sql.execute('select * from professores;')
        tabela = sql.fetchall()
        if sql.rowcount > 0:
            for i in tabela:
                grid.add_row([i[0], i[1], i[2], i[3], i[4]])
            print(grid)
        else:
            print('Não existe professores cadastrado!')
    except Exception as erro:
        print(f'Erro: {erro}')
#-------------------------------------------------
def verificarProfessor(c=0):
    try:
        sql = conn.cursor()
        sql.execute(f'select * from professores where registro={c};')
        tabela = sql.fetchall()
        if sql.rowcount > 0:
            for i in tabela:
                print(f'Nome do professor: {i[1]} ')
            return 'ex'
        else:
            return 'in'

    except Exception as erro:
        return (f'erro {erro} ')
#-----------------------------------------------
def cadastrarProfessor(c=0, nome='', tel='', idade=0, sa=0):
    try:
        sql = conn.cursor()
        sql.execute(f'insert into professores (registro, nomeprof,telefoneprof,idadeprof,salarioprof) values({c},"{nome}","{tel}",{idade},{sa})')
        conn.commit()
        return 'Cadastrado com sucesso!'
    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Ocorreu um erro ao cadastrar'
#---------------------------------------------------
def alterarProfessor(c=0, nome='', tel='', ida=0, sa=0):
    try:
        sql = conn.cursor()
        sql.execute(f'update professores set nomeprof="{nome}",telefoneprof="{tel}",idadeprof={ida},salarioprof={sa} where registro={c};')
        conn.commit()
        return 'Registro atualizado!'

    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Não foi possível atualizar o professor!'
#------------------------------------------------------------
def excluirProfessor(c=0):
    print()
    try:
        sql = conn.cursor()
        sql.execute(f'delete from professores where registro={c};')
        conn.commit()
        return 'Professor deletado com sucesso!'
    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Não foi possível deletar este registro!'
#-----------------------------------------------------------------
def relacaodisxprof(c=0):
    try:
        sql = conn.cursor()
        sql.execute(f'select * from disciplinasxprofessores where codprofessor={c};')
        tabela = sql.fetchall()
        if sql.rowcount > 0:
            return 'ex'
        else:
            return 'in'
    except Exception as erro:
        print(f'Erro: {erro}')

#===============DISCIPLINASxPROFESSORES===================
def mostrarDiscxProfs():
    try:
        grid = PrettyTable(['Código disc no curso', 'disciplina', 'professor', 'curso', 'carga horário', 'ano letivo'])
        sql = conn.cursor()
        sql.execute('select * from disciplinasxprofessores;')
        tabela = sql.fetchall()
        if sql.rowcount > 0:
            for i in tabela:
                sql.execute(f'select * from disciplinas where codigodisc={i[1]};')
                tab1 = sql.fetchall()
                for t1 in tab1:
                    nomed = t1[1]
                sql.execute(f'select * from professores where registro={i[2]};')
                tab1 = sql.fetchall()
                for t1 in tab1:
                    nomeprof = t1[1]
                grid.add_row([i[0], nomed, nomeprof, i[3], i[4], i[5]])
            print(grid)
        else:
            print('não existe disciplinas ligada a professores!')
    except Exception as erro:
        print(f'Erro: {erro} ')
#--------------------------------------------------------
def verificarDiscxProfs(c=''):
    try:
        sql = conn.cursor()
        sql.execute(f'select * from disciplinasxprofessores where codigodisciplinanocurso="{c}";')
        tabela = sql.fetchall()
        if sql.rowcount > 0:
            for i in tabela:
                print(f'código: {i[0]}')
            return 'ex'
        else:
            return 'in'

    except Exception as erro:
        print(f'Erro: {erro} ')
#--------------------------------------------
def verificardisc(c=0):
    try:
        sql = conn.cursor()
        sql.execute(f'select * from disciplinas where codigodisc={c};')
        tabela = sql.fetchall()
        if sql.rowcount > 0:
            for i in tabela:
                print(f'Nome disciplina: {i[1]} ')
            return 1
        else:
            return 0

    except Exception as erro:
        print(f'Erro: {erro} ')
#-------------------------------------------
def verificarprof(c=0):
    try:
        sql = conn.cursor()
        sql.execute(f'select * from professores where registro={c};')
        tabela = sql.fetchall()
        if sql.rowcount > 0:
            for i in tabela:
                print(f'Nome professor: {i[1]} ')
            return 1
        else:
            return 0

    except Exception as erro:
        print(f'Erro: {erro} ')
#-----------------------------------
#----------------------------------------------
def cadastrarDiscxProfs(c='', cc=0, cp=0, cur=0, ch=0, al=0):
    try:
        sql = conn.cursor()
        sql.execute(f'insert into disciplinasxprofessores (codigodisciplinanocurso,coddisciplina,codprofessor,curso,cargahoraria,anoletivo) values("{c}",{cc},{cp},{cur},{ch},{al});')
        conn.commit()
        return 'cadastrado com sucesso!'

    except Exception as erro:
        print(f'Erro {erro} ')
        return 'não foi possível inserir no banco, os dados informados'

def alterarDiscxProfs(c='', cd=0, cp=0, cur=0,ch=0,al=0):
    try:
        sql = conn.cursor()
        sql.execute(f'update disciplinasxprofessores set coddisciplina={cd},codprofessor={cp},curso={cur},cargahoraria={ch},anoletivo={al} where codigodisciplinanocurso="{c}";')
        conn.commit()
        return "atualizado com sucesso!"

    except Exception as erro:
        print(f'Erro: {erro} ')
        return 'não foi possível atualizar!'
#-------------------------------------------------
def excluirDiscxProfs(c=''):
    try:
        sql = conn.cursor()
        sql.execute(f'delete from disciplinasxprofessores where codigodisciplinanocurso="{c}";')
        conn.commit()
        return 'Deletado com sucesso!'

    except Exception as erro:
        print(f' Erro {erro} ')
        return 'Não foi possível deletar este curso'


#================MAIN DISCIPLINAS=============
def maindisciplinas():
    while True:
        print('='*80)
        print('{:^80}'.format('SISTEMA UNIVAP - DISCIPLINAS'))
        print('='*80)

        while True:
            codigodisc = input('Código da disciplina: (0- mostra todas as discs)')
            if codigodisc.isnumeric():
                codigodisc = int(codigodisc)
                break
        if codigodisc == 0:
            mostrartodasDisciplinas()
            continue #volta para o while resp == '1'

        if consultardisciplina(codigodisc) == 'nc':
            nomedisciplina = input('Nome da disciplina: ')
            msg = cadastrardisciplina(codigodisc, nomedisciplina)
            print(msg)
        else:
            op = input('Escolha [A]-alterar [E]-excluir [C]-cancelar operações ==> ').upper()
            while op != 'A' and op != 'E' and op != 'C':
                op = input('Escolha corretamente: [A]-alterar [E]-excluir [C]-cancelar operações ==> ').upper()
            
            if op == 'A':
                print('Codigo da disciplina n pode ser alterado')
                nomedisciplina = input('novo nome da disciplina:  ')
                msg = alterardisciplina(codigodisc, nomedisciplina)
                print(msg)
            elif op == 'E':
                confirma = input('deseja mesmo deletar? S/N  ').upper()
                while confirma != 'S' and confirma != 'N':
                    confirma = input('escolha S/N  ').upper()
                if confirma == 'S':
                    msg = excluirdisciplina(codigodisc)
                else:
                    msg = 'Disciplina não será deletado'
                print(msg)
        print('\n\n')
        print('='*80)

        if input('Deseja continuar no módulo de disciplinas? 1-s ou qualquer tecla-n') == '1':
            continue
        else:
            break
#================MAIN PROFESSORES=============
def mainprofessores():
    while True:
        print('='*80)
        print('{:^80}'.format('SISTEMA UNIVAP - PROFESSORES'))
        print('='*80)

        while True:
            codigo = input('Código dos professores (0 para mostrar todos os professores) --> ')
            if codigo.isnumeric():
                codigo = int(codigo)
                break

        if codigo == 0: #mostrar tudo
            mostrartodosProfessores()
            continue

        if verificarProfessor(codigo) == 'in':
            if input('não existe esse registro, deseja cadastrar? 1-sim/qualquer tecla-não --> ') == '1':
                while True:
                    try:
                        nome = input('Digite o nome do professor:  ')
                        tel = input('Digite o telefone: ')
                        idade = int(input('Digite a idade do professor:  '))
                        salario = float(input('Digite o salário: R$'))
                        msg = cadastrarProfessor(codigo, nome, tel, idade, salario)
                        print(msg)
                        break
                    except:
                        print('algum dado não foi informado corretamente, preenche novamente!\n')
                        print('='*80)
        else:
            op = input('Escolha [A]-alterar [E]-excluir [S]-sair da consulta ==> ').upper()
            while op != 'A' and op != 'E' and op != 'S':
                op = input('Escolha corretamente! [A]-alterar [E]-excluir [S]-sair da consulta ==> ').upper()

            if op == 'A':
                if relacaodisxprof(codigo) == 'in':
                    print('---!!!não é possível alterar o registro!!!---')
                    while True:
                        try:
                            nome = input('Digite o nome do professor:  ')
                            tel = input('Digite o telefone: ')
                            idade = int(input('Digite a idade do professor:  '))
                            salario = float(input('Digite o salário: R$'))
                            break
                        except:
                            print('algum dado não foi informado corretamente, preenche novamente!\n')
                            print('='*80)
                    msg = alterarProfessor(codigo, nome, tel, idade, salario)
                    print(msg)
                else:
                    print('O professor informado está ligado a alguma disciplina!\nlogo não é possível altera-lo')


            elif op == 'E':
                if relacaodisxprof(codigo) == 'in':
                    conf = input('deseja mesmo deletar? S/N  ').upper()
                    while conf != 'S' and conf != 'N':
                        conf = input('escolha S/N  ')
                    if conf == 'S':
                        msg = excluirProfessor(codigo)
                    else:
                        msg = 'Professor não será deletado'
                    print(msg)
                else:
                    print('O professor informado está ligado a alguma disciplina!\nlogo não é possível deleta-lo')
        print('\n\n')
        print('='*80)
        if input('Deseja continuar no módulo de Professores? 1-s ou qualquer tecla-n') == '1':
            continue
        else:
            break
#================MAIN DISCIPLINASxPROFESSORES=============
def maindiscxprofs():
    while True:
        print('='*80)
        print('{:^80}'.format('SISTEMA UNIVAP - DISCIPLINASXPROFESSORES'))
        print('='*80)
        
        cod = input('Digite o codigo de disciplina no curso (0 mostrarar tudo) --> ')
        if cod.isnumeric():
            cod = int(cod)
        
        if cod == 0:
            mostrarDiscxProfs()
            continue

        if verificarDiscxProfs(cod) == 'in':
            if input('não existe dados sobre esse código, deseja cadastrar? 1-sim/qualquer tecla-não') == '1':
                while True:
                    mostrartodasDisciplinas()
                    mostrartodosProfessores()
                    print('acima estão duas tabelas com os códigos de disciplinas e professores!')
                    try:
                        cddisc = int(input('Digite o código da disciplina: '))
                        cdprof = int(input('Digite o registro do professor: '))
                        curso = input('Numero do curso: ')
                        cargah = input('Carga horária: ')
                        anol = input('ano letivo: ')
                        break
                    except:
                        print('algum campo não foi informado corretamente!')
                        print('='*80)
                if verificardisc(cddisc) == 1 and verificarprof(cdprof) == 1:
                    msg = cadastrarDiscxProfs(cod, cddisc, cdprof, curso, cargah, anol)
                    print(msg)
                else:
                    print('o código de disciplina ou do professor não foi cadastrado!')
        else:
            op = input('Escolha [A]-alterar [E]-excluir [S]-sair da consulta ==> ').upper()
            while op != 'A' and op != 'E' and op != 'S':
                op = input('Escolha corretamente! [A]-alterar [E]-excluir [S]-sair da consulta ==> ').upper()
            
            if op == 'A':
                while True:
                    try:
                        mostrartodasDisciplinas()
                        mostrartodosProfessores()
                        cddisc = int(input('Digite o código da disciplina: '))
                        cdprof = int(input('Digite o registro do professor: '))
                        curso = input('Numero do curso: ')
                        cargah = input('Carga horária: ')
                        anol = input('ano letivo: ')
                        break
                    except:
                        print('algum campo não foi informado corretamente!')
                if verificardisc(cddisc) == 1 and verificarprof(cdprof) == 1:
                    msg = alterarDiscxProfs(cod, cddisc, cdprof, curso, cargah, anol)
                    print(msg)
                else:
                    print('o código de disciplina ou do professor não foi cadastrado!')
            elif op == 'E':
                conf = input('deseja mesmo excluir este curso? S/N  ').upper()
                while conf != 'S' and conf != 'N':
                    conf = input('escolha S/N  ').upper()
                if conf == 'S':
                    msg = excluirDiscxProfs(cod)
                else:
                    msg = 'DisciplinasxProfessores não sera deletado'
                print(msg)
        print('\n\n')
        print('='*80)
        if input('Deseja continuar no módulo disciplinasxprofessores? 1-sim/qualquer tecla-não ') == '1':
            continue
        else:
            break

    print()

#=====================MAIN================
if abrirbanco() == 1:
    while True:
        while True:
            try:
                resp = int(input('Escolha um módulo na qual deseja acessar: 1-disciplinas | 2-professores | 3-disciplinasXprofessores\n==> '))
                break
            except:
                print('Insira um valor corretamente!')

        if resp == 1:
            maindisciplinas()
        elif resp == 2:
            mainprofessores()
        elif resp == 3:
            maindiscxprofs()
        
        if input('Deseja continuar o programa? 1-s qualquer tecla-n') == '1':
            continue
        else:
            break
    print('Fim do programa')
    sql.close()
    conn.close()
else:
    print('FIM do programa, tem algum problema na conexão com o banco de dados')

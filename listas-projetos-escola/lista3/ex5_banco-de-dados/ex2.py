import sqlite3
import mysql.connector
from prettytable import PrettyTable
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

def mostrar():
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

def verificar(c=''):
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

    except:
        print(f'')
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

    except:
        print(f'')

def disceprofs():
    try:
        grid = PrettyTable(['Código','Disciplina'])
        sql = conn.cursor()
        sql.execute('select * from disciplinas;')
        tabela = sql.fetchall()
        if sql.rowcount > 0:
            for i in tabela:
                grid.add_row([i[0], i[1]])
            print(grid)
        grid = PrettyTable(['registro','nome','telefone','idade','salario'])
        sql.execute('select * from professores;')
        tabela = sql.fetchall()
        if sql.rowcount > 0:
            for i in tabela:
                grid.add_row([i[0], i[1], i[2], i[3], i[4]])
            print(grid)
    except Exception as erro:
        print(f'Erro {erro} ')

def cadastrar(c='', cc=0, cp=0, cur=0, ch=0, al=0):
    try:
        sql = conn.cursor()
        sql.execute(f'insert into disciplinasxprofessores (codigodisciplinanocurso,coddisciplina,codprofessor,curso,cargahoraria,anoletivo) values("{c}",{cc},{cp},{cur},{ch},{al});')
        conn.commit()
        return 'cadastrado com sucesso!'

    except Exception as erro:
        print(f'Erro {erro} ')
        return 'não foi possível inserir no banco os dados informados'

def alterar(c='', cd=0, cp=0, cur=0,ch=0,al=0):
    try:
        sql = conn.cursor()
        sql.execute(f'update disciplinasxprofessores set coddisciplina={cd},codprofessor={cp},curso={cur},cargahoraria={ch},anoletivo={al} where codigodisciplinanocurso="{c}";')
        conn.commit()
        return "atualizado com sucesso!"

    except Exception as erro:
        print(f'Erro: {erro} ')
        return 'não foi possível atualizar!'

def excluir(c=''):
    try:
        sql = conn.cursor()
        sql.execute(f'delete from disciplinasxprofessores where codigodisciplinanocurso="{c}";')
        conn.commit()
        return 'Deletado com sucesso!'

    except Exception as erro:
        print(f' Erro {erro} ')
        return 'Não foi possível deletar este curso'

'''
================main=================
'''
if abrirbanco() == 1:
    esc = input('Deseja acessar o módulo de disciplinasxprofessores? 1-sim/qualquer tecla-não --> ')
    while esc == '1':
        print('='*80)
        print('{:^80}'.format('SISTEMA UNIVAP - DISCIPLINASXPROFESSORES'))
        print('='*80)
        
        cod = input('Digite o codigo de disciplina no curso (0 mostrarar tudo) --> ')
        if cod.isnumeric():
            cod = int(cod)
        
        if cod == 0:
            mostrar()
            continue

        if verificar(cod) == 'in':
            if input('não existe dados sobre esse código, deseja cadastrar? 1-sim/qualquer tecla-não') == '1':
                while True:
                    disceprofs()
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
                    msg = cadastrar(cod, cddisc, cdprof, curso, cargah, anol)
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
                        cddisc = int(input('Digite o código da disciplina: '))
                        cdprof = int(input('Digite o registro do professor: '))
                        curso = input('Numero do curso: ')
                        cargah = input('Carga horária: ')
                        anol = input('ano letivo: ')
                        break
                    except:
                        print('algum campo não foi informado corretamente!')
                if verificardisc(cddisc) == 1 and verificarprof(cdprof) == 1:
                    msg = alterar(cod, cddisc, cdprof, curso, cargah, anol)
                    print(msg)
                else:
                    print('o código de disciplina ou do professor não foi cadastrado!')
            elif op == 'E':
                conf = input('deseja mesmo excluir este curso? S/N  ').upper()
                while conf != 'S' and conf != 'N':
                    conf = input('escolha S/N  ').upper()
                if conf == 'S':
                    msg = excluir(cod)
                    print(msg)
        print('\n\n')
        print('='*80)
        if input('Deseja continuar o programa? 1-sim/qualquer tecla-não ') == '1':
            continue
        else:           
            print('Fim do programa')
            sql.close()
            conn.close()
            break
else:
    print('não conectou ao banco! - fim do programa')
   


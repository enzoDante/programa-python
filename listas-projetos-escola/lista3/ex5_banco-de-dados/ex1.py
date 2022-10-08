import re
import mysql.connector
from prettytable import PrettyTable

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

def mostrartudo():
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

def verificar(c=0):
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

def cadastrar(c=0, nome='', tel='', idade=0, sa=0):
    try:
        sql = conn.cursor()
        sql.execute(f'insert into professores (registro, nomeprof,telefoneprof,idadeprof,salarioprof) values({c},"{nome}","{tel}",{idade},{sa})')
        conn.commit()
        return 'Cadastrado com sucesso!'
    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Ocorreu um erro no cadastro'

def alterar(c=0, nome='', tel='', ida=0, sa=0):
    try:
        sql = conn.cursor()
        sql.execute(f'update professores set nomeprof="{nome}",telefoneprof="{tel}",idadeprof={ida},salarioprof={sa} where registro={c};')
        conn.commit()
        return 'Registro atualizado!'

    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Não foi possível atualizar o professor!'

def excluir(c=0):
    print()
    try:
        sql = conn.cursor()
        sql.execute(f'delete from professores where registro={c};')
        conn.commit()
        return 'Professor deletado com sucesso!'
    except Exception as erro:
        print(f'Erro: {erro}')
        return 'Não foi possível deletar este registro!'

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

'''
===============main===============
'''
if banco() == 1:
    esc = input('deseja entrar no módulo dos professores? 1-sim / qualquer tecla-não\n')
    while esc == '1':
        print('='*80)
        print('{:^80}'.format('SISTEMA UNIVAP - PROFESSORES'))
        print('='*80)

        while True:
            codigo = input('Código dos professores (0 para mostrar todos os professores) --> ')
            if codigo.isnumeric():
                codigo = int(codigo)
                break

        if codigo == 0: #mostrar tudo
            mostrartudo()
            continue

        if verificar(codigo) == 'in':
            if input('não existe esse registro, deseja cadastrar? 1-sim/qualquer tecla-não --> ') == '1':
                while True:
                    try:
                        nome = input('Digite o nome do professor:  ')
                        tel = input('Digite o telefone: ')
                        idade = int(input('Digite a idade do professor:  '))
                        salario = float(input('Digite o salário: R$'))
                        msg = cadastrar(codigo, nome, tel, idade, salario)
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
                    msg = alterar(codigo, nome, tel, idade, salario)
                    print(msg)
                else:
                    print('O professor informado está ligado a alguma disciplina!\nlogo não é possível altera-lo')


            elif op == 'E':
                if relacaodisxprof(codigo) == 'in':
                    conf = input('deseja mesmo deletar? S/N  ').upper()
                    while conf != 'S' and conf != 'N':
                        conf = input('escolha S/N  ')
                    msg = excluir(codigo)
                    print(msg)
                else:
                    print('O professor informado está ligado a alguma disciplina!\nlogo não é possível deleta-lo')
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
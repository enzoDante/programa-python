from prettytable import PrettyTable
import mysql.connector

def abrebanco():
    try:
        global conn
        conn = mysql.connector.Connect(
            host='localhost', database='univap',user='root',password=''
        )
        if conn.is_connected():
            print('conectado com sucesso')
            global comandosql
            comandosql = conn.cursor()
            comandosql.execute('select database();')
            nomebanco = comandosql.fetchone()
            print(f'banco = {nomebanco}')
            print('='*80)
            return 1
        else:
            print('n conectou')
            return 0
    except Exception as erro:
        print(f'deu erro = {erro} ')
        return 0

def mostrartodas():
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
        return (f'deu eerro {erro} ')

def cadastrardisciplina(cd=0, nd=''):
    try:
        comandosql = conn.cursor()
        comandosql.execute(f'insert into disciplinas(codigodisc, nomedisc) values({cd}, "{nd}");')
        conn.commit()
        return 'Cadastro realizado'
    except Exception as erro:
        print(f'Erro> {erro} ')
        return 'n deu p cadastrar'

def alterardisciplina(cd=0, nomedisciplina=''):
    try:
        comandosql = conn.cursor()
        comandosql.execute(f'Update disciplinas SET nomedisc="{nomedisciplina}" where codigodisc={cd};')
        conn.commit()
        return 'Disciplina atualizado!'
    except Exception as erro:
        print(f'Erro: {erro} ')
        return 'erro n atualizou'

def excluirdisciplina(cd=0):
    try:
        comandosql = conn.cursor()
        comandosql.execute(f'delete from disciplinas where codigodisc={cd};')
        conn.commit()
        return 'deletado'
    except Exception as erro:
        print(f'Erro {erro} ')
        return 'deu ruim n deleto'

'''
=======================começa aq=======================
'''
if abrebanco() == 1:
    resp = input('Deseja entrar no mod disciplinas? (1-Sim/qualquer tecla-Não) ==>  ')
    while resp == '1':
        print('='*80)
        print('{:^80}'.format('SISTEMA UNIVAP DE MERDA - DISCIPLINAS'))
        print('='*80)

        while True:
            codigodisc = input('Código da disciplina: (0- mostra todas as discs)')
            if codigodisc.isnumeric():
                codigodisc = int(codigodisc)
                break
        if codigodisc == 0:
            mostrartodas()
            continue #volta para o while resp == '1'

        if consultardisciplina(codigodisc) == 'nc':
            nomedisciplina = input('Nome da disciplina: ')
            msg = cadastrardisciplina(codigodisc, nomedisciplina)
            print(msg)
        else:
            op = input('Escolha [A]-alterar [E]-excluir [C]-cancelar operações ==> ')
            while op != 'A' and op != 'E' and op != 'C':
                op = input('Escolha corretamente: [A]-alterar [E]-excluir [C]-cancelar operações ==> ')
            
            if op == 'A':
                print('Codigo da disciplina n pode ser alterado')
                nomedisciplina = input('novo nome da disciplina:  ')
                msg = alterardisciplina(codigodisc, nomedisciplina)
                print(msg)
            elif op == 'E':
                confirma = input('deseja mesmo deletar? S/N  ')
                while confirma != 'S' and confirma != 'N':
                    confirma = input('escolha S/N  ')
                msg = excluirdisciplina(codigodisc)
                print(msg)
        print('\n\n')
        print('='*80)

        if input('Deseja continuar o programa? 1-s ou qualquer tecla-n') == '1':
            continue
        else:
            break
        comandosql.close()
        conn.close()
else:
    print('FIM do programa, tem algum problema no banco ou sla')

        
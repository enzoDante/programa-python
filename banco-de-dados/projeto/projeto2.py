#Enzo Dante
#Bruno Braga
#Samuel Pascoal
import mysql.connector
from mysql.connector import Error


try:
    conn = mysql.connector.connect(
        host='localhost',
        database='projetobruno02',
        user='root',
        password=''
    )
    #algumas variáveis aqui==================
    nome = ''
    senha = ''
    usuarios = list()
    colunas_dadosd = ['data', 'derretimento por toneladas', 'nível do mar']
    id_usu = 0
    data_inserida = '00/00/00'#dados segunda tabela
    derreter_ton = 0.0
    nivel_mar = 0.0
    cursor_dados = conn.cursor()


    def cadastroelogin():
        cursor_dados = conn.cursor()
        print('=='*50)
        print('Agora escolha uma das opções:')
        opcao = int(input('cadastrar-1 / logar-2\n'))
        print('=='*30)
        while opcao < 1 or opcao > 2:
            opcao = int(input('Digite 1-cadastrar ou 2-logar!!!\n'))
            print('--'*30)
        
        #usuarios = list() #lista de todos os usuarios
        #cursor_dados = conn.cursor() #cria o cursor do mysql
        sql = f"SELECT * FROM usuario" #comando sql
        cursor_dados.execute(sql) #executa o comando acima
        da = cursor_dados.fetchall() #pega todos os valores da tabela
        usuarios.clear()
        for x in da:
            #adiciona os nomes em uma lista
            usuarios.append(x[1])
            
        #print(usuarios)
        print('=-'*30)
        nome = input('Digite seu nome:\n')
        senha = input('Digite sua senha:\n')
        print('=-'*30)
        #id_usu = 0
        #opção de cadastrar------------------------
        if opcao == 1:

            #verifica se existe o nome digitado na tabela(no caso, na lista), caso n exista irá inseri-lo
            if not nome in usuarios:
                sql = f"INSERT INTO usuario (nome, senha) VALUES('{nome}', '{senha}')"
                cursor_dados.execute(sql) #executado o sql
                conn.commit() #atualiza a tabela
                usuarios.append(nome)
                print('--'*30)
                print(f'Nome inserido, olá {nome}!\n')
                print('--'*30)
                
            #caso conta exista----------------------------------
            else:
                print('=!'*30)
                print('Conta já existente, insira um nome diferente!\n')
                print('=!'*30)    
                while nome in usuarios:
                    print('Nome existente no banco de dados')
                    nome = input('Digite outro nome:\n')
                    print('=-'*30)
                usuarios.append(nome)
                sql = f"INSERT INTO usuario (nome, senha) VALUES('{nome}', '{senha}')"
                cursor_dados.execute(sql)
                conn.commit()
                print('=='*30)
                print(f'Valores inseridos, olá {nome}!')
                print('=='*30)
#=================================================================================
            sql = f"SELECT * FROM usuario WHERE nome='{nome}'"
            cursor_dados.execute(sql)
            da = cursor_dados.fetchall()
            for x in da:
                id_usu = x[0] #retorna o id do usuario, será útil para confirmar o login em outro def
            
            
        #login====================================================
        else:
            while not nome in usuarios:
                print('=!'*30)
                print('Esse nome não está cadastrado!!')
                nome = input('Digite um nome existente: ')
                print('=='*30)
            else:
                sql = f"SELECT * FROM usuario WHERE nome='{nome}' AND senha='{senha}'"
                cursor_dados.execute(sql)
                da = cursor_dados.fetchall()
                print('=='*30)
                for x in da:
                    print(f'Olá {x[1]}! Bem Vindo de volta!')
                    id_usu = x[0]
                print('=='*30)
        cursor_dados.close()#-------------------------------------
        return id_usu
    #===============TUDO QUE O USUÁRIO PODE FAZER========================
    def executandoAtividades(op, nome, id):
        #cursor_dados = conn.cursor()
        if op == 1:
            #INSERIR (Cada usuário só pode inserir uma única vez, as outras são updates!!!)
            print('=='*30)
            data_inserida = input('Digite a data(DD/MM/AAAA HH:MM:SS):  ')
            derreter_ton = float(input('Derretimento por toneladas: '))
            nivel_mar = float(input('Digite o nível do mar em milímetros obtido:  '))
            print('=='*30)
            sql = f"SELECT * FROM dadosd WHERE id_ligado={id}"
            cursor_dados.execute(sql)
            da = cursor_dados.fetchall()
            # essa variável é necessária p fazer a condição abaixo, imagino q o motivo seja o id especificado no where do comando
                    
            if cursor_dados.rowcount != 0:#---------------------------------------------------
                #se ja existe registro na tabela, ele irá somente atualizar a tabela!!!==========
                sql = f"UPDATE dadosd SET data='{data_inserida}',derretimento_ton={derreter_ton}, nivel_mar={nivel_mar} WHERE id_ligado={id}"
                cursor_dados.execute(sql)
                conn.commit()
                print('=='*30)
                print(f'{nome}, seus dados foram atualizados na tabela!\n')
                print('=='*30)
            else:
                
                #===========caso não exista nenhum registro feito por este usuário na tabela:===================
                sql = f"INSERT INTO dadosd values('{data_inserida}',{derreter_ton},{nivel_mar},{id})"
                cursor_dados.execute(sql)
                conn.commit()
                print('=='*30)
                print(f'{nome}, seus dados foram inseridos na tabela!!!\n')
                print('--'*30)
            return
        if op == 2:
            #SELECIONAR (ver as coisas)
            novo_c = conn.cursor() #novo cursor para pegar os nomes da tabela usuario
            sql = f"SELECT nome, id_usuario FROM usuario"
            novo_c.execute(sql)
            da2 = novo_c.fetchall()

            sql = f"SELECT * FROM dadosd"
            cursor_dados.execute(sql)
            da = cursor_dados.fetchall()

            for x in range(0, cursor_dados.rowcount):
                print('==='*30)
                for nomesn in range(0, len(usuarios)):
                    if da2[nomesn][1] == da[x][3]: #verifica se o id na linha nomesn é igual ao id_ligado da linha x
                        print(f'Pesquisador(a): {usuarios[nomesn]}')

                for i in range(0, 3):
                    print(f'{colunas_dadosd[i]}: {da[x][i]}')
                print('==='*30)
            novo_c.close()
            return
        if op == 3:
            #DELETAR (deletar somente oq esse usuário atual inseriu)
            sql = f"SELECT * FROM dadosd WHERE id_ligado={id}"
            cursor_dados.execute(sql)
            da = cursor_dados.fetchall()
            if cursor_dados.rowcount != 0:
                sql = f"DELETE FROM dadosd WHERE id_ligado={id}"
                cursor_dados.execute(sql)
                conn.commit()
                print('=='*30)
                print('Registro deletado!')
                print('--'*30)
            else:
                print('=='*30)
                print(f'{nome}, Você não inseriu nenhum registro!\n')

            #delete from usuario WHERE nome='tal' AND id=212;
            return
    
    def atividadesUsuario(nome, id):
        print('=-'*30)   
        print('Você pode atualizar seus dados, verificar todos os dados e deletar seus dados!!')
        print('Você somente deleta e atualiza dados que você inseriu, dados de outro usuario não será afetado!!!\n')
        opcao = int(input(f'{nome}, Deseja inserir, verificar dados ou excluir os dados? (1-2-3)\n'))
        print('-='*30)
        while opcao < 1 or opcao > 3:
            opcao = int(input('Digite 1-inserir/2-selecionar/3-deletar!\n'))
            print('-'*30)
        executandoAtividades(opcao, nome, id)





    #====================laço de repetição, parte principal do programa======================== 
    #cursor_dados = conn.cursor()
    while True:
        print('=='*30)
        opcao = int(input('você quer cadastrar/logar?\n(1-sim/2-não)\n'))
        while opcao < 1 or opcao > 2:
            opcao = int(input('Digite 1-sim ou 2-não!!!\n'))
            print('--'*30)
        if opcao == 1:
            #==============função de login e cadastro===================
            id = cadastroelogin()
            nome = usuarios[id-1]
            print(nome)

        elif nome != '':
            #cursor_dados = conn.cursor()
            atividadesUsuario(nome, id)
            #utilizando a chave estrangeira, inserir selecionar e deletar!!!! falta somente o deletar!!!!!!
        else:
            print('=!'*30)
            print('Você não fez o login!!!\n')
            print('!='*30)
        print('=='*30)
        opcao = int(input(f'{nome} Você deseja continuar o programa? 1-sim/2-não\n '))
        print('=='*30)
        while opcao < 1 or opcao > 2:
            opcao = int(input('Digite 1-sim/2-não!!!\n'))
            print('-'*30)
        if opcao == 2:
            break
        

    
except Error as e:
    print('Erro de conexão!\n')
finally:
    if conn.is_connected():
        cursor_dados.close()
        conn.close()
        print('='*37)
        print('Programa finalizado! volte sempre ;D')
        print('='*37)





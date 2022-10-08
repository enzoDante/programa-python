import mysql.connector
from prettytable import PrettyTable
grid = PrettyTable(['codigo', "nomes"])
try:
    conn = mysql.connector.Connect(
        host='localhost',
        database='univap',
        user='root',
        password=''
    )
    if conn.is_connected():
        print('conectado com sucesso')
        #informacao = conn.get_server_info()
        #print(f'conectado ao servidor - versão: {informacao}')
        #comandosql = conn.cursor()
        #comandosql.execute('select database();')
        #nomebanco = comandosql.fetchone()
        #print(f'banco = {nomebanco}')
    else:
        print('deu errado')
except Exception as erro:
    print(f'Erro porra {erro}')
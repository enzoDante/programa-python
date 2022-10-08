import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
    database='bancopython',
    user='root',
    password='')

    if connection.is_connected():
        db_info = connection.get_server_info()
        print('Conectado ao mysql versão: ', db_info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print('Você está conectado: ', record)

except Error as e:
    print('Erro na conexão ', e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('mySQL conexão fechada')
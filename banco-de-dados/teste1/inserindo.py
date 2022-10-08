from sqlite3 import connect
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        database='bancopython',
        user='root',
        password=''
    )
    mysql_insert_query = """INSERT INTO aula (id_aula, nome) VALUES (2, 'segundoo dado')"""
    cursor = connection.cursor()
    cursor.execute(mysql_insert_query)
    connection.commit()
    print(cursor.rowcount,' Inserido com sucesso')
    cursor.close()

except Error as e:
    print('Erro ao conectar com mysql ', e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('conexão fechada')
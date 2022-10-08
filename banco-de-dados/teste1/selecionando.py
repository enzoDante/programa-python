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

    sql_select_Query = "select * from aula;"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query) 

    records = cursor.fetchall()
    print("total de registros: ", cursor.rowcount)

    print("\nprintando cada linha: ")
    for row in records:
        print('id_aula = ', row[0], "\n")
        print('nome = ', row[1], "\n")

except Error as e:
    print('erro na conexão ',e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('conexão fechada')
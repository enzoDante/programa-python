import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host='localhost',
        database='bancopython',
        user='root',
        password=''
    )

    id = int(input("Digite o id, ainda nn é auto increment\n"))
    nome = input("digite seu nome\n")

    sql = f"INSERT INTO aula (id_aula, nome) VALUES({id},'{nome}')"
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    print(c.rowcount, " inserido")
    c.close()
    #=========================================
    
    sql = "select * from aula"
    c = conn.cursor()
    c.execute(sql)

    record = c.fetchall()
    print('total de registros: ', c.rowcount)

    for coluna in record:
        print("id_aula = ", coluna[0], "\n")
        print('nome = ', coluna[1], "\n")
    

except Error as e:
    print("erro na conexão")

finally:
    if conn.is_connected():
        c.close()
        conn.close()
        print("cabo")
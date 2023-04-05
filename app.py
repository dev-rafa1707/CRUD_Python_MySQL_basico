import mysql.connector

conexao = mysql.connector.connect(
    host='',
    user='',
    password='',
    database='',
)

cursor = conexao.cursor()




cursor.close()
conexao.close()
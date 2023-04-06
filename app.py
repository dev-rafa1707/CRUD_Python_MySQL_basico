

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='rafa1707',
    database='pybasic',
)

cursor = conexao.cursor()

# CRUD

# CREATE
nomeProduto ='Mouse optico' #Informar o nome do produto
valor=99 #Informar o valor
comando = f'INSERT INTO vendas (nomeProduto, valor) VALUES ("{nomeProduto}",{valor})'
cursor.execute(comando)
conexao.commit() 





cursor.close()
conexao.close()


import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

conexao = mysql.connector.connect(
    host=os.environ.get('DB_HOST'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD'),
    database=os.environ.get('DB_NAME'),
)

cursor = conexao.cursor()

# CRUD

# CREATE
# nomeProduto ='Mouse optico' #Informar o nome do produto
# valor=99 #Informar o valor
# comando = f'INSERT INTO vendas (nomeProduto, valor) VALUES ("{nomeProduto}",{valor})'
# cursor.execute(comando)
# conexao.commit() 

# CREATE
def createCar(nomeProduto, valor):
    comando = f'INSERT INTO vendas (nomeProduto, valor) VALUES ("{nomeProduto}",{valor})'
    cursor.execute(comando)
    conexao.commit()
    return True


#READ ALL
# comando = f'SELECT * FROM vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall() 
# print(resultado)

#READ ALL
def readAll():
    comando = f'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado



#READ BY ID
# idVenda = 4
# comando = f'SELECT * FROM vendas WHERE idVenda = {idVenda}'
# cursor.execute(comando)
# resultado = cursor.fetchall()
# print(resultado)

#UPDATE
# idVenda = 4
# valor = 95
# comando = f'UPDATE vendas SET valor = {valor} WHERE idVenda = {idVenda}'
# cursor.execute(comando)
# conexao.commit()

#DELETE
# idVenda = 2
# comando = f'DELETE FROM vendas WHERE idVenda = {idVenda}'
# cursor.execute(comando)
# conexao.commit()



cursor.close()
conexao.close()


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
def getAll():
    comando = f'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado




# idVenda = 4
# comando = f'SELECT * FROM vendas WHERE idVenda = {idVenda}'
# cursor.execute(comando)
# resultado = cursor.fetchall()
# print(resultado)

#READ BY ID
def getById(idVenda):
    comando = f'SELECT * FROM vendas WHERE idVenda = {idVenda}'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado



#UPDATE
# idVenda = 4
# valor = 95
# comando = f'UPDATE vendas SET valor = {valor} WHERE idVenda = {idVenda}'
# cursor.execute(comando)
# conexao.commit()

#UPDATE
def update(idVenda, nomeProduto, valor):
    comando = f'UPDATE vendas SET nomeProduto = "{nomeProduto}", valor = {valor} WHERE idVenda = {idVenda}'
    cursor.execute(comando)
    conexao.commit()
    return True


#DELETE
# idVenda = 2
# comando = f'DELETE FROM vendas WHERE idVenda = {idVenda}'
# cursor.execute(comando)
# conexao.commit()

########## TESTING AREA ##############



venda = getById(1)
print(venda)

vendas = getAll()
print(vendas)


alteraVenda = update(1,'PC Gamer Extra', 2799)
print(alteraVenda)

venda = getById(1)
print(venda)


cursor.close()
conexao.close()
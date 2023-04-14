

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
def create(nomeProduto, valor):
    comando = f'INSERT INTO vendas (nomeProduto, valor) VALUES ("{nomeProduto}",{valor})'
    cursor.execute(comando)
    conexao.commit()
    return True


#READ ALL
def getAll():
    comando = f'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado



#READ BY ID
def getById(idVenda):
    comando = f'SELECT * FROM vendas WHERE idVenda = {idVenda}'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado



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


# alteraVenda = update(1,'PC Gamer Extra', 2799)
# print(alteraVenda)


novaVenda = create("Cadeira Games", 1789)
print(novaVenda)

vendas = getAll()
print(vendas)

# venda = getById(1)
# print(venda)


cursor.close()
conexao.close()
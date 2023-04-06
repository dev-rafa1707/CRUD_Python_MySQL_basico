

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

#READ ALL
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall() 
print(resultado)


#READ BY ID
idVenda = 4
comando = f'SELECT * FROM vendas WHERE idVenda = {idVenda}'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

#UPDATE
idVenda = 4
valor = 79
comando = f'UPDATE vendas SET valor = {valor} WHERE idVenda = {idVenda}'
cursor.execute(comando)
conexao.commit()

#DELETE
idVenda = 2
comando = f'DELETE FROM vendas WHERE idVenda = {idVenda}'
cursor.execute(comando)
conexao.commit()



cursor.close()
conexao.close()
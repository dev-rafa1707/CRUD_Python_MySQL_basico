# API Python MySQL


### Status:
Finished


### Features
CRUD

* CREATE nem record database
(Criar novo registro de produto)

* READ ALL  the records in database
(Consultar todos os produtos cadastrados)

* READ by id
(Consulta produto por codigo)

* UPDATE by id  Update a record in database using the id
(Edita produto cadastrado)

* DELETE a recdor in database using the id
(Exclui produto cadastrado)


### Requiriments / ré-requisitos
* Python already installed

* MySQL already installed


### How to run the application / Como rodar a aplicação

* Download this project from
(Fazer o download do projeto a partir de)
<p><git@github.com:dev-rafa1707/CRUD_Python_MySQL_basico.git></p>

* Install the driver connection python-mysql
(Instalar o drive de conexão python mysql)
pip install mysql-connector-python

* Set the environment variables using dotenv
(Consfigurar as variáveis de ambiente usando dotenv)
pip install python-dotenv

* Copy .env.example to .env and input the variables as usend in you database
(Copiar o arquivo .env.example para .env e inserir as variáveis conforme o seu banco de dados)
<p>DB_HOST=</p>
DB_USER=
DB_PASSWORD=
DB_NAME=

* Create the table "vendas" in MySQL
(Criar a tabela "vendas" no MySQL)

create table vendas (  
	idVenda int auto_increment,  
    nomeProduto varchar(45) not null,  
    valor int,
    constraint pk_idvenda primary key (idVenda)  
);


* Use app.py to run the operations (CRUD)
(O arquivos app.py é utilizado para processar as operações do CRUD)



### Main commands / Principais comandos
* Update in database / Editar o banco de dados
conexao.commit()

* Read from database / Ler o banco de dados
cursor.fetchall()


### How to test the application / Como testar a aplicação

To test the application just call the function in app.py, passing the information as parameter if necessary, as shown below:


#### Get by Id
venda1 = getById(1)
print(f'Venda 1: {venda1}')

#### Get All
vendas = getAll()
print(vendas)

#### Update
alteraVenda = update(idVenda,'nomeProduto', valor)
print(alteraVenda)

#### Create
novaVenda = create('nomeProduto', valor)
print(novaVenda)

#### Delete
delVenda = delete(idVenda)


### Author
Any question or issue, please contact me
dev-rafa1707
<rafa1707@gmail.com>



### License
No License required 
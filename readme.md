# API Python MySQL


### Status do Projeto:
Finalizado


### Features
CRUD

* Criar novo registro de produto (Create)

* Consultar os produtos cadastrados (Read all)

* Consulta produto por codigo (Read by id)

* Edita produto cadastrado (Update by id)

* Exclui produto cadastrado (Delete)

### Pré-requisitos
* Ter o Python instalado na máquina

* Ter o MySQL instalado na máquina




### Como rodar a aplicação

* Fazer o download do projeto a partir de <git@github.com:dev-rafa1707/CRUD_Python_MySQL_basico.git>.

* Instalar o drive de conexão python mysql / Install the driver connection python-mysql
pip install mysql-connector-python

*  Consfigurar as variáveis de ambiente usando dotenv/ Set the environment variables using dotenv
pip install python-dotenv



### Para testar o projeto



### Principais comandos
* Editar o banco de dados
conexao.commit()

* Ler o banco de dados
cursor.fetchall()


### Estrutura da tabela vendas no MySQL

create table vendas (  
	idVenda int auto_increment,  
    nomeProduto varchar(45) not null,  
    valor int,
    constraint pk_idvenda primary key (idVenda)  
);  
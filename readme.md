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
* Ter o MySQL instalado na máquina

* Instalar o drive de conexão python mysql
pip install mysql-connector-python


### Como rodar a aplicação

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
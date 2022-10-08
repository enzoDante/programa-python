#create database projetobruno02;
use projetobruno02;
/*
create table usuario(
id_usuario int not null primary key auto_increment,
nome varchar(100) not null
);*/
#alter table usuario add column senha varchar(100) not null;

#select * from usuario;
#select * from dadosd;
/*
create table dadosd(
data varchar(100) not null,
derretimento_ton decimal not null,
nivel_mar decimal not null,
id_ligado int not null
);*/
#alter table dadosd add foreign key (id_ligado) references usuario(id_usuario);

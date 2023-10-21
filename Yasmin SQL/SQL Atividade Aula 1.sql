CREATE DATABASE infinityschool;
USE infinityschool;

DROP DATABASE infinityschool;

create table professores(
	id int primary key auto_increment,
    nome varchar(100) not null,
    salario float,
    cpf varchar(20),
    endereco varchar(250) not null
);

alter table professores add dt_nascimento date; 
alter table professores drop column cpf;
alter table professores change endereco endereco_completo varchar(100);
alter table professores add cpf varchar(20);
alter table professores  modify cpf varchar(11);
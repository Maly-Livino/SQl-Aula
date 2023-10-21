#Comentario
-- Comentario também

CREATE DATABASE infinityschool;
USE infinityschool;

DROP DATABASE infinityschool;

CREATE TABLE alunos(
	matricula INT PRIMARY KEY AUTO_INCREMENT,
    nome varchar(100) NOT NULL,
    nota float,
    dt_nascimento date # aaaa-mm-dd
);

alter table alunos add curso varchar(75) default 'Python';

# Como remover uma coluna?

alter table alunos drop column nota;

# Como renomear uma coluna

alter table alunos change dt_nascimento data_nascimento date;

describe alunos;
create table produtos (
	cod int primary key auto_increment,
    nome varchar(100),
    preco float,
    categoria varchar(100)

);

insert into produtos values 
(default,'Mouse',150,'Perifericos'),
(default,'Teclado',210,'Perifericos'),
(default,'Fone',130,'Acessorios'),
(default,'Teclado',210,'Monitores');
select * from produtos;

/*
 < Menor que
 > Maior que 
 >= Maior ou Igual
 <= Menor ou Igual
 Between 
 in
 and,or,not
*/

# Como atualizar um registro?

update produtos set nome = 'Mouse HyperX', preco= 235
where cod = 1;

# Atualizando o preço de todos os perifericos 
update produtos set preco = preco * 0.9
where categoria = 'Perifericos';
select * from produtos;
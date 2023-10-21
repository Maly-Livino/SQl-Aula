select count(*) from ator;

select * from ator where ator_id = 31;

select pais_id from pais where pais = 'Brazil';
select * from pais where pais like 'A%';
select count(pais) from pais where pais like 'A%';
select * from pais where pais like 'P%';
select count(pais) from pais where pais like 'P%';
select * from pais where pais like 'O%';
select count(pais) from pais where pais like 'O%';

select * from pais where pais like 'NA%';
select count(pais) from pais where pais like 'NA%';
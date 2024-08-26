create table IF NOT EXISTS persons(id int primary key auto_increment, name varchar(50) not null, gender varchar(2), location varchar(50), age int check(age > 0));

select * from persons;

insert into persons(name, gender, location, age) values('anagha', 'f', 'hubballi', 18);

insert into persons(name, gender, location) values('anagha', 'f', 'hubballi');

insert into persons(name, gender, location, age) values('rudra', 'm', 'hubballi', 26);

insert into persons(name, gender, age) values('anagha', 'f', 18);

insert into persons(name, gender, location, age) values('agastya', 'm', 'mahabaleshwar', 25);

insert into persons(name) values('anagha');

insert into persons(name, gender) values('anagha', 'f');

insert into persons(name,  age) values('anagha',  18);

insert into persons(name, gender) values('shourya', 'm');

insert into persons(name, gender, location, age) values('alex', 'm', 'ny', 28);

insert into persons(name, gender, location, age) values('rhys', 'm', 'eldora', 28);

insert into persons(name, gender, location, age) values('josh', 'm', 'asia', 28);

select name, location from persons;

select location from persons;

select distinct location from persons;

select * from persons where age > 18;

select * from persons where location = 'hubballi';

select * from persons where age between 25 and 26;

select * from persons where name like 'a____a';

select * from persons where location in('hubballi','ny');

select * from persons where location = null;

select * from persons where location = 'null';

select * from persons where location is null;

select avg(age)  as average_age from persons;

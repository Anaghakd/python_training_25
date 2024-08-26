use anagha_db;

create table employeees(id int primary key auto_increment , name varchar(50) not null, designation varchar(40) not null , technology varchar(30) not null , phone_num bigint unique, commission int, salary float default 0, years_of_exp int);

select * from employeees;

insert into employeees(name, designation , technology, phone_num , commission , salary, years_of_exp) values('anagha', 'COO','IT', 987456321 , 32, 7500, 5)


 into employeees(name, designation , technology, phone_num , commission , salary, years_of_exp) values('anagha', 'COO','IT', 987456321 , 12, 7500, 5)

insert into employees(name, designation , technology, phone_num , commission , salary) values('anagha', 'COO','IT', 987456221 , 32, 7500);

insert into employeees(name, designation , technology, phone_num , commission , salary, years_of_exp) values('anagha', 'COO','IT', 987326321 , 12, 700, 5)

insert into employeees(name, designation , technology, phone_num , commission , salary, years_of_exp) values('anagha', 'COO','IT', 887326321 , 72, 700, 4)

insert into employeees(name, designation , technology, phone_num , commission , salary, years_of_exp) values('anagha', 'COO','IT', 987326321 , 12, 700, 5)

insert into employeees(name, designation , technology, phone_num , commission , salary, years_of_exp) values('rudraa', 'COO','IT', 987326321 , 12, 700, 5)

insert into employeees(name, designation , technology, phone_num , commission , salary, years_of_exp) values('rudraa', 'COO','IT', 987326321 , 12, 700, 5)

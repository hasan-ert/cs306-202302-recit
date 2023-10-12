CREATE TABLE employees(
 eid INT,
 name varchar(50),
 age int,
 primary key (eid)
);

Create Table departments(
	did int,
    dname varchar(50),
    primary key (did)
);

Create table works_in(
	did int,
    eid int,
    primary key(eid,did),
    Foreign Key (eid) References employees(eid),
    Foreign Key (did) References departments(did)
);


insert into employees(name,eid,age) Values ('Ekin',25,23);

insert into departments Values (1,"IT");
insert into departments Values (2,"HR");

Insert into works_in Values (1,55);
Insert into works_in Values (1,10);
Insert into works_in Values (2,25);


SELECT * FROM works_in ;

Delete from works_in where eid = 10;

Delete From employees Where name = 'Hasan';

Drop Table works_in;

Alter table employees 
Rename column eid to emp_id;
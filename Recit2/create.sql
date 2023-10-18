SELECT * FROM recit1_2.employees;

create table students(
	sid int,
    name varchar(25),
    primary key (sid)
);

create table courses(
	cid int,
    name varchar(20),
    primary key (cid)
);

create table enrolled(
	sid int,
    cid int,
    primary key (sid,cid),
    Foreign key (sid) References students(sid) ON DELETE CASCADE
);
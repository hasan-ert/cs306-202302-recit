CREATE TABLE sailors (
	sid INT,
    sname VARCHAR(20),
    rating decimal,
    age INT,
    primary key (sid)
);

CREATE TABLE boats (
	bid INT,
    bname VARCHAR(20),
    color varchar(20),
    primary key (bid)
);
-- CREATE TABLE statements
CREATE TABLE reserves(
	sid INT,
    bid INT,
    primary key(sid,bid),
    foreign key (sid) REFERENCES sailors(sid) ON DELETE CASCADE,
    foreign key (bid) REFERENCES boats(bid) ON DELETE CASCADE
    
);
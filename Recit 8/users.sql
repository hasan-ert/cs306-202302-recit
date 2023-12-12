SELECT * FROM recit8.users;


-- Before adding the index
SET profiling = 1;
SELECT * FROM users_copy WHERE age > 32 and age <54;
SHOW PROFILE;


CREATE INDEX name_ind ON users_copy(first_name);
CREATE INDEX age_ind ON users_copy(age);
Drop INDEX age_ind on users_copy;


-- After adding the index
SET profiling = 1;
SELECT * FROM users WHERE age > 32 and age <54;
SHOW PROFILE;
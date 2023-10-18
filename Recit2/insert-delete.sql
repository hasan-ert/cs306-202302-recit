SELECT * FROM recit1_2.enrolled;

Insert into students values (1,'HASAN');
Insert into students values (2,'Ertugrul');
Insert into students values (3,'Mehmet');

Insert into courses values (306,'Database');
Insert into courses values (307,'OS');

Insert into enrolled values (1,306);
Insert into enrolled values (2,306);
Insert into enrolled values (2,307);

# if you try to delete a record from student table before
# deleting the corresponding rows in a relationship table with 
# a foreign key constraint, it will throw an error

Delete from enrolled where sid = 1;
Delete from students where sid = 1;

Select * from enrolled;

# same thing applies for update as well
UPDATE students SET sid = 5 where sid = 3;



-- Let's add a check constraint to keep our sailors in a given age range
ALTER TABLE sailors
ADD CONSTRAINT age_restriction CHECK(age > 15 and age < 65);

-- Now, test it with some insert operations
INSERT INTO sailors(sid,sname,rating,age) VALUES ("200","David",8,25); -- This one works
INSERT INTO sailors(sid,sname,rating,age) VALUES ("199","Martin",6,14); -- Is not accepted
INSERT INTO sailors(sid,sname,rating,age) VALUES ("157","Abraham",8,80); -- Is not accepted


-- Let's assume we want to have at least 10 sailors in our database
-- So we need a mechanism to check that, why not use triggers then!
DELIMITER // 
-- You can specify the delimiter in your MySQL database 
-- to get rid of any confusion your DBMS might have

-- A basic template for a trigger can be in this format: 
-- create trigger [trigger_name] 
-- [before | after]  
-- {insert | update | delete}  
-- on [table_name]  
-- [for each row]  
-- [trigger_body] 



CREATE TRIGGER sailors_count_check
BEFORE DELETE ON sailors
FOR EACH ROW
BEGIN
	-- If your sailor count is lower than 10
	IF ((SELECT COUNT(*) FROM sailors) <= 10) then 
    -- This signal raises an error and interrupts the insertion
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'There must be at least 10 sailors, you cannot delete any sailor unless you have more than 10';
    END IF;
END//

DELIMITER ;

-- Time for a little test, lets try to delete some records
SELECT COUNT(*) FROM SAILORS; -- 11
SELECT COUNT(*) FROM SAILORS WHERE RATING < 8; -- 5
DELETE FROM sailors where rating < 8;

-- The exception we provided is fired and records are not deleted

DELIMITER //
CREATE TRIGGER sailors_age_fix
BEFORE INSERT ON sailors
FOR EACH ROW
BEGIN
	-- If your sailor count is lower than 10
	IF (new.age <= 15) then 
    -- This signal raises an error and interrupts the insertion
	SET new.age = 16;
    
    END IF;
END//

DELIMITER ;

-- Now, test it with some insert operations
INSERT INTO sailors(sid,sname,rating,age) VALUES ("165","David",8,13); -- This one works and age is inserted as 16


SELECT * FROM sailors_db.sailors;

create table colors (
	color_id INT,
    color VARCHAR(10),
    PRIMARY KEY (color_id)
);

INSERT INTO colors Values (1,"red");
INSERT INTO colors Values (2,"blue");
INSERT INTO colors Values (3,"green");

Alter table boats
ADD CONSTRAINT boat_color CHECK (color IN (Select colors from Colors));


DELIMITER //

CREATE TRIGGER check_color 
BEFORE INSERT ON boats
FOR EACH ROW
Begin
	IF (NEW.color IN (Select color from Colors)) THEN
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'There must be at least 10 sailors, you cannot delete any sailor unless you have more than 10';
    END IF;
END//

DELIMITER ;


Drop trigger check_color;
INSERT INTO boats Values (900,"Interlake","red");

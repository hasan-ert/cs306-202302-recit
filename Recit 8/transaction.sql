CREATE TABLE bank_accounts (
    account_id INT PRIMARY KEY,
    balance DECIMAL(10, 2),
    CHECK (balance > 0)
);

CREATE TABLE transaction_history (
    transaction_id INT PRIMARY KEY auto_increment,
    account_id INT,
    amount DECIMAL(10, 2),
    transaction_type VARCHAR(10),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES bank_accounts(account_id)
);


-- Insert sample data into bank_accounts table
INSERT INTO bank_accounts (account_id, balance) VALUES
(1, 200.00), -- Account 1 with a balance of $1000.00
(2, 500.00),  -- Account 2 with a balance of $500.00
(3, 1500.00), -- Account 3 with a balance of $1500.00
(4, 200.00);   -- Account 4 with a balance of $200.00


-- Insert sample data into transaction_history table
INSERT INTO transaction_history (account_id, amount, transaction_type) VALUES
(1, -100.00, 'debit'), -- Debit of $100.00 from Account 1
(2, 100.00, 'credit'), -- Credit of $100.00 to Account 2
(1, -50.00, 'debit'),  -- Debit of $50.00 from Account 1
(3, 200.00, 'credit'), -- Credit of $200.00 to Account 3
(2, -30.00, 'debit'),  -- Debit of $30.00 from Account 2
(4, 100.00, 'credit'); -- Credit of $100.00 to Account 4


-- Use this to shutdown auto committing after each statement
SET autocommit = 0;


Update bank_accounts SET balance = 300 where account_id = 1;
-- Start a transaction
START TRANSACTION;

-- Update the balance for the source account (assuming account_id 1 is the source)
UPDATE bank_accounts SET balance = balance - 100.00 WHERE account_id = 1;

-- Insert a record into the transaction history for the debit
INSERT INTO transaction_history (account_id, amount, transaction_type) VALUES (1, -100.00, 'debit');

-- Update the balance for the destination account (assuming account_id 2 is the destination)
UPDATE bank_accounts SET balance = balance + 100.00 WHERE account_id = 2;

-- Insert a record into the transaction history for the credit
INSERT INTO transaction_history (account_id, amount, transaction_type) VALUES (2, 100.00, 'credit');

-- Commit the transaction if everything is successful
COMMIT;



-- What about a transaction that would fail?
-- Start a transaction
START TRANSACTION;

-- Attempt to transfer $200 from Account 1 to Account 2
UPDATE bank_accounts SET balance = balance - 200.00 WHERE account_id = 1; -- This will make the balance negative

Rollback;

select * from bank_accounts;
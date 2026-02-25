DROP DATABASE IF EXISTS personal_finance;
CREATE DATABASE personal_finance;
USE personal_finance;

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_date DATE,
    description VARCHAR(255),
    category VARCHAR(100),
    amount DECIMAL(12,2),
    type VARCHAR(20)
);
LOAD DATA INFILE 
'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Personal_Finance_Dataset.csv'
INTO TABLE transactions
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@Date, @Description, @Category, @Amount, @Type)
SET
transaction_date = @Date,
description = @Description,
category = @Category,
amount = @Amount,
type = @Type;
SELECT COUNT(*) FROM transactions;
SELECT * FROM transactions;

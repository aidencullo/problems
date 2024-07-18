DROP DATABASE IF EXISTS company;
CREATE DATABASE company;
USE company;


-- Create the log table
CREATE TABLE log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(255),
    log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    salary DECIMAL(10, 2)
);

-- Create the trigger
DELIMITER //

CREATE TRIGGER after_insert_employee
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    INSERT INTO log (message)
    VALUES ('A new employee has been added.');
END;

//

DELIMITER ;

INSERT INTO employees (name, salary)
VALUES ('John Doe', 1000),
       ('Jane Doe', 1500),
       ('Jim Doe', 2000);

UPDATE employees
SET salary = 2500;

SELECT * FROM log;

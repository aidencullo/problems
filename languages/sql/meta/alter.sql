DROP DATABASE IF EXISTS sales_db;
CREATE DATABASE sales_db;
USE sales_db;

CREATE TABLE employees(
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100),
  department VARCHAR(100),
  salary DECIMAL(10, 2)
);

INSERT INTO employees(name, department)
VALUES
  ('John Doe', 'HR');

ALTER TABLE employees
ALTER COLUMN salary SET DEFAULT 50000.00;

INSERT INTO employees(name, department)
VALUES
  ('John Doe', 'HR');

SELECT * FROM employees;

ALTER TABLE employees
DROP COLUMN salary;

SELECT * FROM employees;

ALTER TABLE employees
MODIFY COLUMN department VARCHAR(200);

SELECT * FROM employees;

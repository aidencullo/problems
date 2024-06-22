DROP DATABASE IF EXISTS retail_db;
		CREATE DATABASE retail_db;

USE retail_db;

-- setup

-- Create employees table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date DATE
);

-- Insert data into employees table
INSERT INTO employees (employee_id, first_name, last_name, department, salary, hire_date)
VALUES 
(1, 'Alice', 'Smith', 'HR', 35000.00, '2018-05-15'),
(2, 'Bob', 'Johnson', 'IT', 45000.00, '2017-10-20'),
(3, 'Charlie', 'Brown', 'Sales', 60000.00, '2019-02-28'),
(4, 'David', 'Lee', 'IT', 55000.00, '2020-01-10'),
(5, 'Emma', 'Wilson', 'HR', 38000.00, '2016-08-05');

-- Create customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50),
    registration_date DATE
);

-- Insert data into customers table
INSERT INTO customers (customer_id, customer_name, city, registration_date)
VALUES 
(1, 'John Doe', 'New York', '2017-06-12'),
(2, 'Jane Smith', 'Los Angeles', '2018-03-25'),
(3, 'Michael Johnson', 'Chicago', '2019-09-10');

-- Create orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    order_amount DECIMAL(10, 2)
);

-- Insert data into orders table
INSERT INTO orders (order_id, customer_id, order_date, order_amount)
VALUES
(101, 1, '2023-06-01', 1500.00),
(102, 1, '2024-01-05', 2000.00),
(103, 2, '2024-02-12', 500.00),
(104, 3, '2024-03-18', 3000.00),
(105, 3, '2024-05-06', 2500.00);



-- Filter employees who belong to the IT department.



SELECT *
  FROM employees
 WHERE department = 'IT';




-- List customers who registered before January 1, 2019.


SELECT *
  FROM customers
 WHERE registration_date < DATE('2019-01-01');

-- Display orders placed in the year 2024.

SELECT *
  FROM orders
 WHERE YEAR(order_date) = 2024;

-- Show employees hired after January 1, 2019, with a salary greater than 50000.


SELECT *
  FROM employees
 WHERE hire_date > DATE('2019-01-01')
   AND salary > 50000;


-- Find customers from Chicago or New York.


SELECT *
  FROM customers
 WHERE city IN ('Chicago', 'New York');

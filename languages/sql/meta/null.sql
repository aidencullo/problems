DROP DATABASE IF EXISTS retail_db;
		CREATE DATABASE retail_db;

USE retail_db;

-- setup


-- Explain the difference between IS NULL and = when comparing values in SQL. Provide an example.

-- = will not properly compare NULL, ie it simply won't work. IS NULL is the correct way to compare NULL values.

-- CREATE TABLE students (
--   id INT PRIMARY KEY AUTO_INCREMENT,
--   name VARCHAR(50)
-- );

-- INSERT INTO students (name) VALUES
-- ('Alice'),
-- (NULL),
-- ('Bob'),
-- ('Charlie');

-- SELECT * FROM students WHERE name IS NULL;
-- SELECT * FROM students WHERE name = NULL;




-- -- Write a query to find all employees who do not have a supervisor. Assume the supervisor_id column contains NULL for such employees.



-- SELECT employee_id, first_name, last_name
-- FROM employees
-- WHERE supervisor_id IS NULL;




-- How would you replace NULL values in a column with a default value using SQL? Demonstrate with a column bonus in the employees table, where the default value is 0.



-- UPDATE employees
--  SET bonus = 0
--  WHERE bonus IS NULL;


-- SELECT employee_id, name, COALESCE(bonus, 0) AS bonus
-- FROM employees;


-- Given a table orders with columns order_id, customer_id, and order_date, write a query to count the number of orders placed by each customer, including customers with no orders (NULL). Assume a separate customers table.


-- Create customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50)
);

-- Create orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Insert data into customers table
INSERT INTO customers (customer_id, customer_name)
VALUES 
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie'),
(4, 'David');

-- Insert data into orders table
INSERT INTO orders (order_id, customer_id, order_date)
VALUES
(101, 1, '2024-06-01'),
(102, 1, '2024-06-05'),
(103, 2, '2024-06-02'),
(104, 3, '2024-06-03'),
(105, 3, '2024-06-06');


SELECT c.customer_id, COUNT(o.order_id) AS order_count
  FROM customers c
       LEFT JOIN orders o
	   ON c.customer_id = o.customer_id
 GROUP BY c.customer_id;




-- How can you update a table to set a column's NULL values to a specific value? Update the phone_number column in the contacts table to 'N/A' where it is NULL.


UPDATE contacts
   SET phone_number = 'N/A'
 WHERE phone_number IS NULL;

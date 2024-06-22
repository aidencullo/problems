DROP DATABASE IF EXISTS retail_db;
		CREATE DATABASE retail_db;

USE retail_db;

-- setup


-- Explain the difference between IS NULL and = when comparing values in SQL. Provide an example.

-- = will not properly compare NULL, ie it simply won't work. IS NULL is the correct way to compare NULL values.

CREATE TABLE students (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50)
);

INSERT INTO students (name) VALUES
('Alice'),
(NULL),
('Bob'),
('Charlie');

SELECT * FROM students WHERE name IS NULL;
SELECT * FROM students WHERE name = NULL;




-- Write a query to find all employees who do not have a supervisor. Assume the supervisor_id column contains NULL for such employees.

-- How would you replace NULL values in a column with a default value using SQL? Demonstrate with a column bonus in the employees table, where the default value is 0.

-- Given a table orders with columns order_id, customer_id, and order_date, write a query to count the number of orders placed by each customer, including customers with no orders (NULL). Assume a separate customers table.

-- How can you update a table to set a column's NULL values to a specific value? Update the phone_number column in the contacts table to 'N/A' where it is NULL.


DROP DATABASE IF EXISTS retail_db;
		CREATE DATABASE retail_db;

USE retail_db;

-- setup



-- Create employees table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    salary DECIMAL(10, 2),
    start_date DATE
);

-- Insert data into employees table
INSERT INTO employees (employee_id, first_name, last_name, salary, start_date)
VALUES 
(1, 'Alice', 'Smith', 28000, '2019-05-10'),
(2, 'Bob', 'Johnson', 35000, '2020-01-15'),
(3, 'Charlie', 'Brown', 60000, '2018-08-20'),
(4, 'David', 'Lee', 75000, '2017-10-01'),
(5, 'Emma', 'Wilson', 40000, '2021-03-25');

-- Create customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50)
);

-- Insert data into customers table
INSERT INTO customers (customer_id, customer_name)
VALUES 
(1, 'John Doe'),
(2, 'Jane Smith'),
(3, 'Michael Johnson');

-- Create orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_amount DECIMAL(10, 2),
    order_date DATE
);

-- Insert data into orders table
INSERT INTO orders (order_id, customer_id, order_amount, order_date)
VALUES
(101, 1, 1500.00, '2024-06-01'),
(102, 1, 2000.00, '2024-06-05'),
(103, 2, 500.00, '2024-06-02'),
(104, 3, 3000.00, '2024-06-03'),
(105, 3, 2500.00, '2024-06-06');

-- Question 5: Display order status based on order date
SELECT 
    order_id,
    order_date,
    CASE 
        WHEN DATEDIFF(CURRENT_DATE, order_date) > 30 THEN 'More than 30 days ago'
        WHEN DATEDIFF(CURRENT_DATE, order_date) BETWEEN 10 AND 30 THEN 'Between 10 and 30 days ago'
        ELSE 'Within the last 10 days'
    END AS order_status
FROM orders;





-- Write a query to categorize employees based on their salary into three groups: 'Low', 'Medium', and 'High'. Assume the salary ranges are: Low for salaries less than 30000, Medium for salaries between 30000 and 60000 (inclusive), and High for salaries greater than 60000. Include columns for employee_id, first_name, last_name, and salary_group.



SELECT employee_id, first_name, last_name,
       CASE
	   WHEN salary < 30000 THEN 'Low'
	   WHEN salary BETWEEN 30000 AND 60000 THEN 'Medium'
	   ELSE 'High'
       END AS salary_group
  FROM employees;



-- Create a report that calculates the total amount spent per customer on orders. Include columns for customer_id, customer_name, and total_spent. Sort the results in descending order of total_spent.


SELECT c.customer_id, c.customer_name, SUM(o.order_amount) AS total_spent
  FROM orders o
       JOIN customers c
       ON o.customer_id = c.customer_id
 GROUP BY o.customer_id
 ORDER BY SUM(o.order_amount) DESC;


-- Display a list of employees with their start_date and a new column 'employment_duration' that shows how long each employee has been employed in years, rounded to two decimal places.


SELECT employee_id, first_name, last_name, start_date,
       ROUND(DATEDIFF(CURRENT_DATE, start_date) / 365, 2) AS employment_duration
  FROM employees;




-- List all customers along with a column 'order_status' that indicates whether a customer has placed any orders ('Yes' or 'No').




SELECT c.customer_id, c.customer_name,
       CASE
       WHEN COUNT(o.order_id) > 0 THEN 'Yes'
       ELSE 'No'
       END AS order_status
  FROM orders o
       JOIN customers c
	   ON o.customer_id = c.customer_id
 GROUP BY o.customer_id;




-- For each order in the orders table, display the order_id, order_date, and a column 'order_status' that indicates if the order was placed more than 30 days ago, between 30 and 10 days ago, or within the last 10 days.



SELECT o.order_id, o.order_date,
       CASE
       WHEN DATEDIFF(CURRENT_DATE, o.order_date) <= 10 THEN 'Within the last 10 days'
       WHEN DATEDIFF(CURRENT_DATE, o.order_date) BETWEEN 10 AND 30 THEN 'Between 10 and 30 days ago'
       ELSE 'more than 30 days ago'
       END AS order_status
  FROM orders o;

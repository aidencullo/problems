DROP DATABASE IF EXISTS testdb;
CREATE DATABASE testdb;

USE testdb;

-- setup

-- Create table orders
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    order_amount DECIMAL(10, 2)
);

-- Insert data into orders
INSERT INTO orders (order_id, customer_id, order_date, order_amount) VALUES
(1, 101, '2023-01-15', 150.00),
(2, 102, '2023-02-20', 200.00),
(3, 101, '2023-03-10', 50.00),
(4, 103, '2022-12-01', 100.00),
(5, 104, '2023-05-25', 300.00);

-- Create table sales
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    store_id INT,
    sale_date DATE,
    sale_amount DECIMAL(10, 2)
);

-- Insert data into sales
INSERT INTO sales (sale_id, product_id, store_id, sale_date, sale_amount) VALUES
(1, 201, 301, '2023-01-10', 500.00),
(2, 202, 302, '2023-02-15', 300.00),
(3, 201, 301, '2023-03-20', 200.00),
(4, 203, 303, '2023-04-25', 400.00),
(5, 202, 302, '2023-05-30', 600.00);

-- Create table employees
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    department_id INT,
    salary DECIMAL(10, 2),
    hire_date DATE
);

-- Insert data into employees
INSERT INTO employees (employee_id, department_id, salary, hire_date) VALUES
(1, 10, 70000.00, '2020-01-15'),
(2, 20, 80000.00, '2019-03-20'),
(3, 10, 75000.00, '2018-05-10'),
(4, 30, 90000.00, '2017-08-01'),
(5, 20, 85000.00, '2021-11-25'),
(6, 10, 72000.00, '2022-02-15'),
(7, 10, 68000.00, '2023-04-18'),
(8, 30, 93000.00, '2016-07-12'),
(9, 20, 78000.00, '2020-09-30'),
(10, 10, 71000.00, '2018-12-21');

-- Create table customers
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100)
);

-- Insert data into customers
INSERT INTO customers (customer_id, customer_name) VALUES
(101, 'Alice Smith'),
(102, 'Bob Johnson'),
(103, 'Charlie Brown'),
(104, 'Diana Prince');

-- Create table transactions
CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    customer_id INT,
    transaction_date DATE,
    transaction_amount DECIMAL(10, 2)
);

-- Insert data into transactions
INSERT INTO transactions (transaction_id, customer_id, transaction_date, transaction_amount) VALUES
(1, 101, '2023-01-01', 100.00),
(2, 102, '2023-02-15', 200.00),
(3, 101, '2023-03-10', 300.00),
(4, 103, '2023-04-20', 400.00),
(5, 104, '2023-05-25', 500.00);

-- Create table page_views
CREATE TABLE page_views (
    user_id INT,
    page_url VARCHAR(255),
    view_date DATE
);

-- Insert data into page_views
INSERT INTO page_views (user_id, page_url, view_date) VALUES
(1, 'http://example.com/home', '2023-01-01'),
(2, 'http://example.com/about', '2023-02-01'),
(1, 'http://example.com/contact', '2023-03-01'),
(3, 'http://example.com/home', '2023-01-15'),
(4, 'http://example.com/about', '2023-04-01'),
(2, 'http://example.com/contact', '2023-05-01');



-- 1. Basic Aggregation
-- Question: Given a table orders with columns order_id, customer_id, order_date, and order_amount, write a query to find the total order amount for each customer.

SELECT customer_id, SUM(order_amount) AS total_order_amount
  FROM orders
 GROUP BY customer_id;


-- 2. Aggregation with Filtering
-- Question: Given the same orders table, write a query to find the total order amount for each customer, but only for orders placed in the year 2023.


SELECT customer_id, SUM(order_amount) AS total_order_amount
  FROM orders
 WHERE YEAR(order_date) = 2023
 GROUP BY customer_id;

-- 3. Aggregation with Multiple Columns
-- Question: Given a table sales with columns product_id, store_id, sale_date, and sale_amount, write a query to find the total sales for each product in each store.

SELECT product_id, store_id, SUM(sale_amount)
  FROM sales
 GROUP BY product_id, store_id;


-- 4. Aggregation with HAVING Clause
-- Question: Given a table employees with columns employee_id, department_id, salary, and hire_date, write a query to find the average salary for each department, but only for departments with more than 5 employees.

SELECT COUNT(*), AVG(salary) AS avg_salary
  FROM employees
 GROUP BY department_id
HAVING COUNT(*) > 5;


-- 5. Aggregation with JOIN
-- Question: Given two tables, orders (with columns order_id, customer_id, order_date, and order_amount) and customers (with columns customer_id and customer_name), write a query to find the total order amount for each customer name.

UPDATE orders
   SET order_amount = NULL
 WHERE customer_id = 103;
SELECT * FROM customers;
SELECT * FROM orders;

SELECT c.customer_name, COALESCE(SUM(o.order_amount), 0) AS total_order_amount
  FROM customers AS c
       JOIN orders AS o
	   ON c.customer_id = o.customer_id
 GROUP BY c.customer_name;

-- 6. Aggregation with DATE Functions
-- Question: Given a table sales with columns sale_id, product_id, sale_date, and sale_amount, write a query to find the total sales for each month in the year 2023.

SELECT SUM(sale_amount)
  FROM sales
 GROUP BY MONTH(sale_date);


-- 7. Aggregation and Subqueries
-- Question: Given a table transactions with columns transaction_id, customer_id, transaction_date, and transaction_amount, write a query to find the customer who has the highest total transaction amount.

SELECT customer_id
  FROM (
    SELECT customer_id, SUM(transaction_amount) AS total_transaction_amount
      FROM transactions
     GROUP BY customer_id
     ORDER BY total_transaction_amount DESC
     LIMIT 1	   
  ) AS max_total_transaction_amount;


-- 8. Aggregation with DISTINCT
-- Question: Given a table page_views with columns user_id, page_url, and view_date, write a query to find the number of unique users who viewed each page URL.
 
SELECT page_url, COUNT(DISTINCT user_id) AS distinct_user_count
FROM page_views
GROUP BY page_url;

-- 9. Aggregation with CASE Statement
-- Question: Given a table orders with columns order_id, customer_id, order_date, and order_status (which can be 'completed', 'pending', or 'cancelled'), write a query to find the total number of orders for each status.

-- 10. Aggregation with Window Functions
-- Question: Given a table sales with columns sale_id, product_id, sale_date, and sale_amount, write a query to find the cumulative sales amount for each product, ordered by sale date.

DROP DATABASE IF EXISTS testdb;
CREATE DATABASE testdb;

USE testdb;

-- 1. Basic Aggregation
-- Question: Given a table orders with columns order_id, customer_id, order_date, and order_amount, write a query to find the total order amount for each customer.

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    order_amount DECIMAL(10, 2)
);

INSERT INTO orders (order_id, customer_id, order_date, order_amount) VALUES
(1, 101, '2023-01-15', 150.00),
(2, 102, '2023-02-20', 200.00),
(3, 101, '2023-03-10', 50.00),
(4, 103, '2022-12-01', 100.00),
(5, 104, '2023-05-25', 300.00);

SELECT customer_id, SUM(order_amount) AS total_order_amount
  FROM orders
GROUP BY customer_id;

DROP DATABASE IF EXISTS retail_db;
		CREATE DATABASE retail_db;

USE retail_db;


-- Create the sales table
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    sale_amount DECIMAL(10, 2),
    sale_date DATE
);

-- Insert sample data into the sales table
INSERT INTO sales (sale_id, product_name, sale_amount, sale_date) VALUES
(1, 'Product A', 100.00, '2022-01-15'),
(2, 'Product B', 150.00, '2022-02-10'),
(3, 'Product A', 200.00, '2022-03-05'),
(4, 'Product C', 50.00, '2022-03-20'),
(5, 'Product A', 300.00, '2022-04-15'),
(6, 'Product B', 250.00, '2022-04-25'),
(7, 'Product A', 400.00, '2022-05-10'),
(8, 'Product C', 100.00, '2022-06-15'),
(9, 'Product B', 300.00, '2022-06-20'),
(10, 'Product A', 500.00, '2022-07-05'),
(11, 'Product A', 600.00, '2021-12-25'), -- This sale should be filtered out by the WHERE clause
(12, 'Product B', 700.00, '2021-11-15'), -- This sale should be filtered out by the WHERE clause
(13, 'Product C', 200.00, '2021-10-05'); -- This sale should be filtered out by the WHERE clause


-- Write a query to find the total sales amount for each product that has more than 3 sales, and filter out sales that occurred before the year 2022. The query should demonstrate the difference between using the WHERE clause and the HAVING clause.

SELECT 
    product_name, 
    SUM(sale_amount) AS total_amount
FROM 
    sales
WHERE 
    YEAR(sale_date) > 2021
GROUP BY 
    product_name
HAVING 
    COUNT(*) > 3;

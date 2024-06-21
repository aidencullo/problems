DROP DATABASE IF EXISTS retail_db;
		CREATE DATABASE retail_db;

USE retail_db;

-- Write a query to find the total sales amount for each product, including cases where the sale_amount is NULL. For products with NULL values in sale_amount, assume the sale amount is 0. Additionally, include only those products that have at least 3 sales.


-- Step 1: Create the sales table
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    sale_amount DECIMAL(10, 2),
    sale_date DATE
);

-- Step 2: Populate the sales table with sample data
INSERT INTO sales (sale_id, product_name, sale_amount, sale_date) VALUES
(1, 'Product A', 100.00, '2022-01-15'),
(2, 'Product B', 150.00, '2022-02-10'),
(3, 'Product A', 200.00, '2022-03-05'),
(4, 'Product C', NULL, '2022-03-20'),
(5, 'Product A', 300.00, '2022-04-15'),
(6, 'Product B', 250.00, '2022-04-25'),
(7, 'Product A', 400.00, '2022-05-10'),
(8, 'Product C', 100.00, '2022-06-15'),
(9, 'Product B', NULL, '2022-06-20'),
(10, 'Product A', 500.00, '2022-07-05'),
(11, 'Product A', NULL, '2022-08-10'),
(12, 'Product B', 700.00, '2022-09-15'),
(13, 'Product C', 200.00, '2022-10-05');


SELECT
    product_name,
    COUNT(*) AS total_sales_count,
    SUM(COALESCE(sale_amount, 0)) AS total_sales_amount
FROM 
    sales
GROUP BY 
    product_name
HAVING 
    COUNT(*) >= 3;


-- | product_name | total_sales | total_sales_amount |
-- |--------------|-------------|--------------------|
-- | Product A    | 5           | 1500.00            |
-- | Product B    | 3           | 1100.00            |
-- | Product C    | 3           | 300.00             |

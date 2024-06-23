DROP DATABASE IF EXISTS retail_db;
		CREATE DATABASE retail_db;

USE retail_db;
-- Create the sales table
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    amount DECIMAL(10, 2)
);

-- Insert sample data into the sales table
INSERT INTO sales (sale_id, product_id, amount) VALUES
(1, 1, 100.00),
(2, 1, 150.00),
(3, 1, 200.00),
(4, 1, 250.00),
(5, 2, 300.00),
(6, 2, 120.00),
(7, 2, 450.00),
(8, 2, 200.00),
(9, 3, 500.00),
(10, 3, 220.00),
(11, 3, 320.00),
(12, 3, 410.00);
-- Find the top 3 sales amounts for each product.


WITH highest_sales AS (
  SELECT
    product_id,
    amount,
    ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY amount DESC) AS rn
  FROM sales
)
SELECT
  product_id,
  amount
FROM
  highest_sales
WHERE
  rn <= 3;

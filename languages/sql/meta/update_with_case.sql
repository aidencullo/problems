DROP DATABASE IF EXISTS retail_db;
		CREATE DATABASE retail_db;

USE retail_db;

-- Create a sample products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10, 2),
    stock_quantity INT
);

-- Insert sample data
INSERT INTO products (product_id, product_name, category, price, stock_quantity)
VALUES 
    (1, 'Laptop', 'Electronics', 999.99, 50),
    (2, 'T-shirt', 'Clothing', 19.99, 200),
    (3, 'Coffee Maker', 'Appliances', 79.99, 30),
    (4, 'Smartphone', 'Electronics', 599.99, 100),
    (5, 'Running Shoes', 'Footwear', 89.99, 75);

-- Practice Question:
-- Update the prices of products based on their category and stock quantity:
-- - Increase the price of 'Electronics' items by 10% if their stock quantity is less than 75
-- - Decrease the price of 'Clothing' items by 5% if their stock quantity is more than 150
-- - Increase the price of all other items by 2% if their stock quantity is between 25 and 100 (inclusive)
-- For all other cases, keep the price unchanged.

-- Write an UPDATE statement using a CASE expression to implement these price changes.


UPDATE products
SET price = 
    CASE
    WHEN category = 'Electronics' AND stock_quantity < 75 THEN price * 1.10
    WHEN category = 'Clothing' AND stock_quantity > 150 THEN price * .95
    WHEN category NOT IN ('Electronics', 'Clothing') AND stock_quantity BETWEEN 25 AND 100 THEN price * 1.02
    ELSE price
    END;

-- UPDATE products
-- SET price = 
--     CASE 
--         WHEN category = 'Electronics' AND stock_quantity < 75 THEN price * 1.10
--         WHEN category = 'Clothing' AND stock_quantity > 150 THEN price * 0.95
--         WHEN category NOT IN ('Electronics', 'Clothing') AND stock_quantity BETWEEN 25 AND 100 THEN price * 1.02
--         ELSE price
--     END;

SELECT * FROM products;


-- Updated products table:
-- | product_id | product_name  | category    | price    | stock_quantity |
-- |------------|---------------|-------------|----------|----------------|
-- | 1          | Laptop        | Electronics | 1099.99  | 50             |
-- | 2          | T-shirt       | Clothing    | 18.99    | 200            |
-- | 3          | Coffee Maker  | Appliances  | 81.59    | 30             |
-- | 4          | Smartphone    | Electronics | 599.99   | 100            |
-- | 5          | Running Shoes | Footwear    | 91.79    | 75             |

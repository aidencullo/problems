CREATE DATABASE IF NOT EXISTS TestDB;

USE TestDB;

-- Drop the orders table if it exists (for reusability)
DROP TABLE IF EXISTS orders;

-- Create the orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    order_date DATE,
    amount DECIMAL(10, 2)
);

-- Insert sample data into the orders table
INSERT INTO orders (order_id, order_date, amount) VALUES 
(1, '2024-01-01', 100.00),
(2, '2024-01-02', 150.00),
(3, '2024-01-03', 200.00),
(4, '2024-01-04', 250.00),
(5, '2024-01-05', 300.00);

-- Query to calculate the moving average of amounts with a window of 2 preceding rows and the current row
SELECT 
    order_id, 
    order_date, 
    amount, 
    AVG(amount) OVER (ORDER BY order_date ROWS BETWEEN 2 PRECEDING AND 1 PRECEDING) AS moving_avg
FROM 
    orders;

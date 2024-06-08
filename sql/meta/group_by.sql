DROP DATABASE IF EXISTS test_db;
CREATE DATABASE test_db;
USE test_db;

CREATE TABLE sales (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product VARCHAR(50),
    amount INT,
    tax INT
);

INSERT INTO sales (product, amount, tax) VALUES
('apple', 10, 1),
('apple', 20, 2),
('banana', 30, 3),
('banana', 40, 4),
('banana', 50, 5),
('cherry', 60, 6),
('cherry', 70, 6),
('cherry', 80, 8),
('cherry', 90, 9),
('cherry', 100, 10);


SELECT product, SUM(amount)
FROM sales
GROUP BY product;

SELECT product, COUNT(*)
FROM sales
GROUP BY product;

SELECT product, AVG(amount)
FROM sales
GROUP BY product;

SELECT product, tax, SUM(amount)
FROM sales
GROUP BY product, tax;

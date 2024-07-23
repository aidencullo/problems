DROP DATABASE IF EXISTS company;
CREATE DATABASE company;
USE company;

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    sex VARCHAR(10)
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    price FLOAT
);

CREATE TABLE transactions (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    created_at DATETIME,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Insert data into users table
INSERT INTO users (id, name, sex) VALUES
(1, 'Alice', 'Female'),
(2, 'Bob', 'Male'),
(3, 'Carol', 'Female'),
(4, 'Dave', 'Male');

-- Insert data into products table
INSERT INTO products (id, name, price) VALUES
(1, 'Product A', 10.0),
(2, 'Product B', 20.0),
(3, 'Product C', 30.0);

-- Insert data into transactions table
INSERT INTO transactions (id, user_id, created_at, product_id, quantity) VALUES
(1, 1, '2023-01-01 10:00:00', 1, 2),  -- Alice bought 2 of Product A
(2, 1, '2023-01-02 11:00:00', 2, 1),  -- Alice bought 1 of Product B
(3, 2, '2023-01-03 12:00:00', 1, 1),  -- Bob bought 1 of Product A
(4, 2, '2023-01-04 13:00:00', 3, 1),  -- Bob bought 1 of Product C
(5, 3, '2023-01-05 14:00:00', 2, 2),  -- Carol bought 2 of Product B
(6, 4, '2023-01-06 15:00:00', 1, 1),  -- Dave bought 1 of Product A
(7, 4, '2023-01-07 16:00:00', 3, 1);  -- Dave bought 1 of Product C

SELECT
    sex,
    AVG(quantity * price) AS avg_transaction_amount,
    COUNT(DISTINCT t.id) AS total_transactions,
    COUNT(DISTINCT p.id) AS total_products_bought,
    COUNT(DISTINCT u.id) AS total_users
FROM
    transactions t
JOIN
    products p
ON
    p.id = t.product_id
JOIN
    users u
ON
    u.id = t.user_id
GROUP BY
    sex;

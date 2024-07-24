 /*
 BACKGROUND:

 The following schema is a subset of a relational database of a grocery store
 chain. This chain sells many products of different product classes to its
 customers across its different stores. It also conducts many different
 promotion campaigns.
 The relationship between the four tables we want to analyze is depicted below:

       # sales                                # products
       +------------------+---------+         +---------------------+---------+
       | product_id       | INTEGER |>--------| product_id          | INTEGER |
       | store_id         | INTEGER |    +---<| product_class_id    | INTEGER |
       | customer_id      | INTEGER |    |    | brand_name          | VARCHAR |
  +---<| promotion_id     | INTEGER |    |    | product_name        | VARCHAR |
  |    | store_sales      | DECIMAL |    |    | is_low_fat_flg      | TINYINT |
  |    | store_cost       | DECIMAL |    |    | is_recyclable_flg   | TINYINT |
  |    | units_sold       | DECIMAL |    |    | gross_weight        | DECIMAL |
  |    | transaction_date | DATE    |    |    | net_weight          | DECIMAL |
  |    +------------------+---------+    |    +---------------------+---------+
  |                                      |
  |    # promotions                      |    # product_classes
  |    +------------------+---------+    |    +---------------------+---------+
  +----| promotion_id     | INTEGER |    +----| product_class_id    | INTEGER |
       | promotion_name   | VARCHAR |         | product_subcategory | VARCHAR |
       | media_type       | VARCHAR |         | product_category    | VARCHAR |
       | cost             | DECIMAL |         | product_department  | VARCHAR |
       | start_date       | DATE    |         | product_family      | VARCHAR |
       | end_date         | DATE    |         +---------------------+---------+
       +------------------+---------+
 */
 /*
 PROMPT:
 -- What are the top five (ranked in decreasing order)
 -- single-channel media types that correspond to the most money
 -- the grocery chain had spent on its promotional campaigns?

 Single Media Channel Types are promotions that contain only one media type.

 EXPECTED OUPTUT:
 Note: Please use the column name(s) specified in the expected output in your solution.
 +---------------------------+------------+
 | single_channel_media_type | total_cost |
 +---------------------------+------------+
 | In-Store Coupon           | 70800.0000 |
 | Street Handout            | 70627.0000 |
 | Radio                     | 60192.0000 |
 | Sunday Paper              | 56994.0000 |
 | Product Attachment        | 50815.0000 |
 +---------------------------+------------+
 
-------------- PLEASE WRITE YOUR SQL SOLUTION BELOW THIS LINE ----------------
 */


DROP DATABASE IF EXISTS grocery_store;
		CREATE DATABASE grocery_store;

USE grocery_store;


-- Create table for sales
CREATE TABLE sales (
    product_id INTEGER,
    store_id INTEGER,
    customer_id INTEGER,
    promotion_id INTEGER,
    store_sales DECIMAL(10, 2),
    store_cost DECIMAL(10, 2),
    units_sold DECIMAL(10, 2),
    transaction_date DATE
);

-- Create table for products
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_class_id INTEGER,
    brand_name VARCHAR(100),
    product_name VARCHAR(100),
    is_low_fat_flg TINYINT,
    is_recyclable_flg TINYINT,
    gross_weight DECIMAL(10, 2),
    net_weight DECIMAL(10, 2)
);

-- Create table for promotions
CREATE TABLE promotions (
    promotion_id INTEGER PRIMARY KEY,
    promotion_name VARCHAR(100),
    media_type VARCHAR(100),
    cost DECIMAL(10, 2),
    start_date DATE,
    end_date DATE
);

-- Create table for product_classes
CREATE TABLE product_classes (
    product_class_id INTEGER PRIMARY KEY,
    product_subcategory VARCHAR(100),
    product_category VARCHAR(100),
    product_department VARCHAR(100),
    product_family VARCHAR(100)
);

-- Insert sample data into products table
INSERT INTO products (product_id, product_class_id, brand_name, product_name, is_low_fat_flg, is_recyclable_flg, gross_weight, net_weight)
VALUES
    (1, 101, 'Brand1', 'Product1', 1, 0, 1.5, 1.2),
    (2, 102, 'Brand2', 'Product2', 0, 1, 2.0, 1.7),
    (3, 103, 'Brand3', 'Product3', 1, 1, 3.0, 2.5),
    (4, 104, 'Brand4', 'Product4', 0, 0, 1.0, 0.8);

-- Insert sample data into promotions table
INSERT INTO promotions (promotion_id, promotion_name, media_type, cost, start_date, end_date)
VALUES
    (1, 'Promotion1', 'In-Store Coupon', 5000.00, '2023-01-01', '2023-01-31'),
    (2, 'Promotion2', 'Radio', 8000.00, '2023-02-15', '2023-03-15'),
    (3, 'Promotion3', 'Sunday Paper', 6000.00, '2023-03-01', '2023-03-31'),
    (4, 'Promotion4', 'Street Handout', 7000.00, '2023-04-10', '2023-04-30'),
    (5, 'Promotion5', 'Product Attachment', 4000.00, '2023-05-05', '2023-05-31'),
    (6, 'Promotion6', 'In-Store Coupon', 7000.00, '2023-06-15', '2023-06-30'),
    (7, 'Promotion7', 'Radio', 12000.00, '2023-07-01', '2023-07-31');

-- Insert sample data into product_classes table
INSERT INTO product_classes (product_class_id, product_subcategory, product_category, product_department, product_family)
VALUES
    (101, 'Subcategory1', 'Category1', 'Department1', 'Family1'),
    (102, 'Subcategory2', 'Category1', 'Department2', 'Family2'),
    (103, 'Subcategory3', 'Category2', 'Department3', 'Family3'),
    (104, 'Subcategory4', 'Category2', 'Department4', 'Family4');

-- Insert sample data into sales table
INSERT INTO sales (product_id, store_id, customer_id, promotion_id, store_sales, store_cost, units_sold, transaction_date)
VALUES
    (1, 1, 1001, 1, 1500.00, 1200.00, 100, '2023-01-05'),
    (2, 2, 1002, 2, 2000.00, 1800.00, 120, '2023-02-20'),
    (3, 1, 1003, 3, 3000.00, 2500.00, 150, '2023-03-15'),
    (4, 3, 1004, 4, 800.00, 700.00, 50, '2023-04-25'),
    (1, 2, 1005, 5, 1200.00, 1000.00, 80, '2023-05-10'),
    (2, 1, 1006, 6, 1800.00, 1500.00, 100, '2023-06-20'),
    (3, 3, 1007, 7, 2500.00, 2200.00, 130, '2023-07-05');

SELECT
media_type as single_channel_media_type,
SUM(cost) as total_cost
FROM
promotions
WHERE
media_type NOT LIKE '%,%'
GROUP BY
media_type
ORDER BY
SUM(cost) DESC
LIMIT
5

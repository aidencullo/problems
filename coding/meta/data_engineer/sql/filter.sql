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
 -- What percent of all products in the grocery chain's catalog
 -- are both low fat and recyclable?
 

 EXPECTED OUTPUT:
 Note: Please use the column name(s) specified in the expected output in your solution.
 +----------------------------+
 | pct_low_fat_and_recyclable |
 +----------------------------+
 |         15.384615384615385 |
 +----------------------------+

 -------------- PLEASE WRITE YOUR SQL SOLUTION BELOW THIS LINE ---------------- 
 */


DROP DATABASE IF EXISTS testDb;
CREATE DATABASE testDb;
USE testDb;

-- Create the tables
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_class_id INTEGER,
    brand_name VARCHAR(255),
    product_name VARCHAR(255),
    is_low_fat_flg TINYINT,
    is_recyclable_flg TINYINT,
    gross_weight DECIMAL,
    net_weight DECIMAL
);

CREATE TABLE product_classes (
    product_class_id INTEGER PRIMARY KEY,
    product_subcategory VARCHAR(255),
    product_category VARCHAR(255),
    product_department VARCHAR(255),
    product_family VARCHAR(255)
);

CREATE TABLE promotions (
    promotion_id INTEGER PRIMARY KEY,
    promotion_name VARCHAR(255),
    media_type VARCHAR(255),
    cost DECIMAL,
    start_date DATE,
    end_date DATE
);

CREATE TABLE sales (
    product_id INTEGER,
    store_id INTEGER,
    customer_id INTEGER,
    promotion_id INTEGER,
    store_sales DECIMAL,
    store_cost DECIMAL,
    units_sold DECIMAL,
    transaction_date DATE,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (promotion_id) REFERENCES promotions(promotion_id)
);

-- Insert sample data into product_classes
INSERT INTO product_classes (product_class_id, product_subcategory, product_category, product_department, product_family)
VALUES 
(1, 'Dairy', 'Food', 'Grocery', 'Perishables'),
(2, 'Beverages', 'Drinks', 'Grocery', 'Non-Perishables'),
(3, 'Snacks', 'Food', 'Grocery', 'Non-Perishables');

-- Insert sample data into products
INSERT INTO products (product_id, product_class_id, brand_name, product_name, is_low_fat_flg, is_recyclable_flg, gross_weight, net_weight)
VALUES 
(1, 1, 'BrandA', 'Milk', 1, 1, 1.0, 0.9),
(2, 2, 'BrandB', 'Juice', 0, 1, 1.5, 1.4),
(3, 3, 'BrandC', 'Chips', 0, 0, 0.5, 0.4);

-- Insert sample data into promotions
INSERT INTO promotions (promotion_id, promotion_name, media_type, cost, start_date, end_date)
VALUES 
(1, 'PromoA', 'TV', 1000.0, '2024-01-01', '2024-01-10'),
(2, 'PromoB', 'Online', 500.0, '2024-02-01', '2024-02-05'),
(3, 'PromoC', 'Radio', 700.0, '2024-03-01', '2024-03-15');

-- Insert sample data into sales
INSERT INTO sales (product_id, store_id, customer_id, promotion_id, store_sales, store_cost, units_sold, transaction_date)
VALUES 
(1, 1, 1, 1, 10.0, 8.0, 1, '2024-01-01'), -- First day of PromoA
(2, 1, 2, 1, 20.0, 16.0, 2, '2024-01-10'), -- Last day of PromoA
(3, 2, 3, 1, 15.0, 12.0, 1.5, '2024-01-05'), -- During PromoA
(1, 2, 4, 2, 12.0, 9.0, 1, '2024-02-01'), -- First day of PromoB
(2, 2, 5, 2, 18.0, 14.0, 1.5, '2024-02-05'), -- Last day of PromoB
(3, 1, 6, 2, 16.0, 13.0, 1.6, '2024-02-03');







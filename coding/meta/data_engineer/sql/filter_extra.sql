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

-- Question: What is the total sales amount for each product category?


SELECT
SUM(store_sales) AS total_sales_amount,
FROM product_classes pc
LEFT JOIN products p
ON p.product_class_id = pc.product_class_id
LEFT JOIN sales s
ON p.product_id = s.product_id
GROUP BY product_category


-- Question: How many unique customers purchased products during each promotion campaign?

SELECT
COUNT(DISTINCT customer_id) AS unique_customers
FROM sales s
JOIN promotions p
ON s.promotion_id = p.promotion_id
GROUP BY promotion_name

-- Question: Which store had the highest number of units sold for recyclable products?


SELECT
store_id
FROM
sales s
JOIN products p
ON s.product_id = p.product_id
WHERE is_recyclable_flg = 1
GROUP BY store_id
ORDER BY SUM(units_sold) DESC
LIMIT 1


-- Question: What is the average cost of promotions for each media type?

SELECT
media_type,
AVG(cost) AS avg_cost
FROM promotions
GROUP BY media_type

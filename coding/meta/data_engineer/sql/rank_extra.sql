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

-- What is the total number of units sold for each brand?
SELECT
SUM(units_sold) as total_units_sold
FROM
products p
LEFT JOIN sales s
ON p.product_id = s.product_id
GROUP BY brand_name


-- What is the average gross and net weight of products in each product category?



SELECT
AVG(net_weight) as avg_net_weight
FROM
products p
LEFT JOIN product_classes pc
GROUP BY product_category


-- Which customers made the highest total purchase amount, and what are their total purchases?

SELECT
customer_id,
SUM(store_sales) as total_purchases
FROM sales
GROUP BY customer_id

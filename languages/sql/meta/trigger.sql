-- Example task: Create a trigger that logs INSERT operations on an orders table to a log table.

DROP DATABASE IF EXISTS company;
CREATE DATABASE company;
USE company;

CREATE TABLE orders(
order_id INT PRIMARY KEY AUTO_INCREMENT,
price INT
);

CREATE TABLE log(
id INT PRIMARY KEY AUTO_INCREMENT,
message TEXT
);

DELIMITER //

CREATE TRIGGER after_insert_orders
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    INSERT INTO log (message)
    VALUES ('New order was inserted');
END;

//

DELIMITER ;

INSERT INTO orders (price)
VALUES
(100),
(200),
(300);

SELECT * FROM log;

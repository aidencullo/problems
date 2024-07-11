DROP DATABASE IF EXISTS company;
CREATE DATABASE company;

USE company;

-- Create the Salesperson table
CREATE TABLE Salesperson (
    ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Salary DECIMAL(10, 2)
);

-- Insert data into the Salesperson table
INSERT INTO Salesperson (ID, Name, Age, Salary) VALUES
(1, 'Abe', 61, 140000),
(2, 'Bob', 34, 44000),
(5, 'Chris', 34, 40000),
(7, 'Dan', 41, 52000),
(8, 'Ken', 57, 115000),
(11, 'Joe', 38, 38000);

-- Create the Orders table
CREATE TABLE Orders (
    Number INT PRIMARY KEY,
    order_date DATE,
    cust_id INT,
    salesperson_id INT,
    Amount DECIMAL(10, 2),
    FOREIGN KEY (salesperson_id) REFERENCES Salesperson(ID)
);

-- Insert data into the Orders table
INSERT INTO Orders (Number, order_date, cust_id, salesperson_id, Amount) VALUES
(10, '1996-08-02', 4, 2, 540),
(20, '1999-01-30', 4, 8, 1800),
(30, '1995-07-14', 9, 1, 460),
(40, '1998-01-29', 7, 2, 2400),
(50, '1998-02-03', 6, 7, 600),
(60, '1998-03-02', 6, 7, 720),
(70, '1998-05-06', 9, 7, 150);


SELECT
    name,
    (SELECT COUNT(*) FROM Orders o WHERE s.id = o.salesperson_id) AS num_orders
FROM
    Salesperson s
HAVING
    num_orders >= 2


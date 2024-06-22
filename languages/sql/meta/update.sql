DROP DATABASE IF EXISTS retail_db;
		CREATE DATABASE retail_db;

USE retail_db;

-- setup

-- Create employees table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    manager_id INT,
    hire_date DATE
);

-- Populate employees table
INSERT INTO employees (employee_id, first_name, last_name, department, salary, manager_id, hire_date)
VALUES
    (101, 'John', 'Doe', 'IT', 75000.00, 100, '2015-01-15'),
    (102, 'Jane', 'Smith', 'Sales', 60000.00, 101, '2017-03-20'),
    (103, 'Michael', 'Johnson', 'IT', 78000.00, 100, '2016-06-10'),
    (104, 'Emily', 'Davis', 'HR', 70000.00, 101, '2018-02-05'),
    (105, 'William', 'Wilson', 'Sales', 58000.00, 102, '2019-04-30');



-- Create orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    order_date DATE,
    status VARCHAR(50)
);

-- Populate orders table
INSERT INTO orders (order_id, order_date, status)
VALUES
    (1, '2023-05-10', 'Pending'),
    (2, '2023-06-15', 'Shipped'),
    (3, '2023-07-20', 'Pending'),
    (4, '2023-08-05', 'Delivered');

-- Create shipments table
CREATE TABLE shipments (
    shipment_id INT PRIMARY KEY,
    order_id INT,
    shipment_date DATE
);

-- Populate shipments table
INSERT INTO shipments (shipment_id, order_id, shipment_date)
VALUES
    (101, 2, '2023-06-20'),
    (102, 4, '2023-08-10'),
    (103, 1, '2023-05-15');

-- Create students table
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    final_score INT,
    grade VARCHAR(2)
);

-- Populate students table
INSERT INTO students (student_id, student_name, final_score)
VALUES
    (1, 'Alice', 85),
    (2, 'Bob', 75),
    (3, 'Charlie', 92),
    (4, 'Diana', 68),
    (5, 'Eve', 78);


-- 1. Update Based on Join
-- Update the orders table to set the status column to 'Shipped' for all orders that have a corresponding record in the shipments table.


UPDATE orders AS o
SET o.status = 'Shipped'
WHERE o.order_id IN (
    SELECT order_id
    FROM shipments
);

-- orders table:
-- | order_id | order_date | status   |
-- |----------|------------|----------|
-- | 1        | 2023-05-10 | Shipped  |
-- | 2        | 2023-06-15 | Shipped  |
-- | 3        | 2023-07-20 | Pending  |
-- | 4        | 2023-08-05 | Shipped  |




-- 2. Conditional Update
-- Increase the salary of employees in the 'IT' department by 5% if their current salary is below 80000.

UPDATE employees
SET salary = salary * 1.05
 WHERE department = 'IT' AND salary < 80000;


-- | employee_id | first_name | last_name | department | salary   | manager_id | hire_date  |
-- |-------------|------------|-----------|------------|----------|------------|------------|
-- | 101         | John       | Doe       | IT         | 78750.00 | 100        | 2015-01-15 |
-- | 102         | Jane       | Smith     | Sales      | 60000.00 | 101        | 2017-03-20 |
-- | 103         | Michael    | Johnson   | IT         | 81900.00 | 100        | 2016-06-10 |
-- | 104         | Emily      | Davis     | HR         | 70000.00 | 101        | 2018-02-05 |
-- | 105         | William    | Wilson    | Sales      | 58000.00 | 102        | 2019-04-30 |



-- 3. Update Using Subquery
-- Set the manager_id of each employee to the employee_id of the employee who has the highest salary in their department.

CREATE TEMPORARY TABLE department_max_salary AS
  SELECT e.department, MAX(e.salary) AS max_salary
  FROM employees e
  GROUP BY e.department;

CREATE TEMPORARY TABLE pared_down_employee AS
  SELECT e.employee_id, e.department, e.salary
  FROM employees e;

CREATE TEMPORARY TABLE employee_max_salary AS
  SELECT p.employee_id, p.department, p.salary, d.max_salary
  FROM pared_down_employee p
  JOIN department_max_salary d
  ON p.department = d.department
  AND p.salary = d.max_salary;

UPDATE employees e
       JOIN employee_max_salary ems
       ON e.department = ems.department
   SET e.manager_id = ems.employee_id;

SELECT * FROM employees;


-- Updated employees table:
-- | employee_id | first_name | last_name | department | salary   | manager_id | hire_date  |
-- |-------------|------------|-----------|------------|----------|------------|------------|
-- | 101         | John       | Doe       | IT         | 78750.00 | 103        | 2015-01-15 |
-- | 102         | Jane       | Smith     | Sales      | 60000.00 | 102        | 2017-03-20 |
-- | 103         | Michael    | Johnson   | IT         | 81900.00 | 103        | 2016-06-10 |
-- | 104         | Emily      | Davis     | HR         | 70000.00 | 104        | 2018-02-05 |
-- | 105         | William    | Wilson    | Sales      | 58000.00 | 102        | 2019-04-30 


-- 4. Update with Case Statement
-- Update the grade column of the students table based on their final_score as follows:

-- If final_score is between 90 and 100, set grade to 'A'.
-- If final_score is between 80 and 89, set grade to 'B'.
-- If final_score is between 70 and 79, set grade to 'C'.
-- Otherwise, set grade to 'F'.


-- UPDATE employees e
-- JOIN temp_lowest_salary_employee t
-- ON 1 = 1
-- SET e.manager_id = CASE
--     WHEN t.employee_id IS NOT NULL THEN t.employee_id
--     ELSE e.manager_id
-- END;



-- 5. Update Using Multiple Tables
-- Update the employees table to reflect a 10% increase in salary for employees who work in departments where the average salary is above 70000.


-- These scenarios cover different aspects of using the UPDATE statement in SQL, including joins, subqueries, conditional updates, and updates based on calculations and conditions. Practice solving these scenarios to improve your SQL proficiency!

DROP DATABASE IF EXISTS retail_db;
		CREATE DATABASE retail_db;

USE retail_db;


-- Create departments table
CREATE TABLE departments (
  dept_id INT PRIMARY KEY,
  dept_name VARCHAR(50)
);

-- Create employees table
CREATE TABLE employees (
  emp_id INT PRIMARY KEY,
  emp_name VARCHAR(50),
  dept_id INT,
  salary DECIMAL(10, 2),
  hire_date DATE,
  FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- Insert data into departments table
INSERT INTO departments (dept_id, dept_name) VALUES
(1, 'HR'),
(2, 'Finance'),
(3, 'IT');

-- Insert data into employees table
INSERT INTO employees (emp_id, emp_name, dept_id, salary, hire_date) VALUES
(1, 'Alice', 1, 60000.00, '2020-01-15'),
(2, 'Bob', 1, 55000.00, '2019-05-20'),
(3, 'Charlie', 2, 70000.00, '2018-08-10'),
(4, 'David', 2, 75000.00, '2021-02-28'),
(5, 'Eve', 3, 65000.00, '2022-04-05'),
(6, 'Frank', 3, 60000.00, '2020-11-12');




-- Practice Questions:
-- Question 1:
-- Retrieve the names of employees who earn more than the average salary in the Finance department.


SELECT emp_name
  FROM employees
 WHERE salary > (
   SELECT AVG(salary)
     FROM employees
    WHERE dept_id = 2	  
 );


-- emp_name
-- --------
-- David




-- Question 2:
-- Find the department(s) with the highest average salary among its employees.

SELECT dept_name
  FROM departments
 WHERE dept_id = (
   SELECT dept_id
     FROM employees
    GROUP BY dept_id
    ORDER BY AVG(salary) DESC	  
    LIMIT 1
 );

-- dept_name
-- ---------
-- Finance


-- Question 3:
-- List the employees who joined after Eve in the same department.

-- Question 4:
-- Count the number of employees in each department and display the department names with more than two employees.

-- Question 5:
-- Identify employees who have a salary higher than any employee in the IT department.

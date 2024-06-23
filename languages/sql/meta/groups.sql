DROP DATABASE IF EXISTS retail_db;
		CREATE DATABASE retail_db;

USE retail_db;

-- setup
-- Create a table for employees
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    EmployeeName VARCHAR(100),
    DepartmentID INT,
    Salary DECIMAL(10, 2)
);

-- Insert some sample data into Employees table
INSERT INTO Employees (EmployeeID, EmployeeName, DepartmentID, Salary)
VALUES 
    (1, 'John Doe', 1, 50000.00),
    (2, 'Jane Smith', 1, 60000.00),
    (3, 'Michael Johnson', 2, 55000.00),
    (4, 'Emily Davis', 2, 52000.00),
    (5, 'David Brown', 3, 48000.00),
    (6, 'Sarah Wilson', 3, 51000.00);

-- Create a table for departments
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100)
);

-- Insert some sample data into Departments table
INSERT INTO Departments (DepartmentID, DepartmentName)
VALUES 
    (1, 'Engineering'),
    (2, 'Marketing'),
    (3, 'Sales');

-- Certainly! Here are 5 SQL interview questions focused on groupings, without the answers:

-- 1. **Count of Employees per Department:**
--    How would you write a SQL query to retrieve the count of employees in each department?


SELECT employees.department, COUNT(*) AS employee_count
  FROM employees
 GROUP BY employees.department;



-- 2. **Average Salary per Department:**
--    Write a SQL query to find the average salary of employees in each department.

 
SELECT employees.department, AVG(employees.salary) AS avg_salary
  FROM employees
 GROUP BY employees.department;




-- 3. **Maximum Salary in each Department:**
--    Can you write a SQL query to find the maximum salary earned by any employee in each department?


 
SELECT employees.department, MAX(employees.salary) AS max_salary
  FROM employees
 GROUP BY employees.department;



-- 4. **List of Departments with more than 2 Employees:**
--    Write a SQL query to list departments that have more than 2 employees.



 
SELECT employees.department, COUNT(*) AS employee_count
  FROM employees
 GROUP BY employees.department
HAVING COUNT(*) > 2;



-- 5. **Sum of Salaries for each Department:**
--    How would you write a SQL query to calculate the total salary expenditure for each department?



 
SELECT employees.department, SUM(employees.salary) AS total_salary
  FROM employees
 GROUP BY employees.department;

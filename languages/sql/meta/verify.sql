DROP DATABASE IF EXISTS retail_db;
		CREATE DATABASE retail_db;

USE retail_db;

CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    EmployeeName VARCHAR(100),
    Salary DECIMAL(10, 2),
    DepartmentID INT
);

CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100)
);

CREATE TABLE StudentScores (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(100),
    ExamScore DECIMAL(5, 2)
);

CREATE TABLE Sales (
    SaleID INT PRIMARY KEY,
    SaleDate DATE,
    Revenue DECIMAL(10, 2)
);

INSERT INTO Employees (EmployeeID, EmployeeName, Salary, DepartmentID) VALUES
(1, 'Alice', 60000, 1),
(2, 'Bob', 70000, 2),
(3, 'Charlie', NULL, 1),
(4, 'David', 80000, 2),
(5, 'Eve', 90000, NULL);

INSERT INTO Departments (DepartmentID, DepartmentName) VALUES
(1, 'HR'),
(2, 'Engineering'),
(3, 'Sales');

INSERT INTO StudentScores (StudentID, StudentName, ExamScore) VALUES
(1, 'Frank', 85),
(2, 'Grace', 90),
(3, 'Heidi', NULL),
(4, 'Ivan', 95),
(5, 'Judy', 70);

INSERT INTO Sales (SaleID, SaleDate, Revenue) VALUES
(1, '2024-01-05', 1000),
(2, '2024-01-15', 1500),
(3, '2024-06-10', NULL),
(4, '2024-02-15', 2000),
(5, '2024-03-05', 2500);





-- Employee Salaries and Department Names:
-- Write a query to list all employees, their salaries, and their respective department names. Include employees who don't have a department assigned and handle NULL values for salary by showing 'Unknown' for such employees.

SELECT
  EmployeeName,
  COALESCE(Salary, 'Unknown') AS Salary,
  COALESCE(DepartmentName, 'No Department') AS DepartmentName
  FROM Employees
       LEFT JOIN Departments
	   ON Employees.DepartmentID = Departments.DepartmentID;

       










-- Average Exam Scores:
-- Write a query to calculate the average exam score for students. Handle NULL exam scores by excluding them from the average calculation. Ensure the result set still includes students with NULL scores, displaying their names and a message indicating they haven't taken the exam.

SELECT
  StudentName,
  COALESCE(AVG(ExamScore), 'No exam taken') AS AverageScore
  FROM StudentScores
 GROUP BY StudentName;









-- Sales Revenue by Month:
-- Write a query to calculate the total sales revenue for each month. Include months where the revenue might be NULL and display 'No sales' for such months.




SELECT
  MONTH(SaleDate) AS Month,
  COALESCE(SUM(Revenue), 'No sales') AS TotalRevenue
FROM Sales
GROUP BY MONTH(SaleDate);

-- Top Paid Employees per Department:
-- Write a query to find the highest-paid employee in each department. Handle cases where some employees may not have a department assigned by including them in a separate category labeled 'No Department'.


WITH highest_salaries AS (
  SELECT
    DepartmentID,
    EmployeeName,
    Salary,
    ROW_NUMBER() OVER (PARTITION BY DepartmentID ORDER BY Salary DESC) AS rn
  FROM Employees
)

SELECT
  COALESCE(DepartmentName, 'No Department') AS DepartmentName,
  EmployeeName,
  Salary
  FROM highest_salaries hs
       LEFT JOIN Departments d
	   ON hs.DepartmentID = d.DepartmentID
 WHERE rn = 1;


-- Ranking Students with Exam Scores:
-- Write a query to rank students based on their exam scores in descending order. Include students who have not taken the exam (NULL scores) at the end of the ranking with a message indicating they haven't taken the exam.

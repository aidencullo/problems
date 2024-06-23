DROP DATABASE IF EXISTS retail_db;
		CREATE DATABASE retail_db;

USE retail_db;

-- Table for employees
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    EmployeeName VARCHAR(100),
    DepartmentID INT,
    Salary DECIMAL(10, 2)
);

-- Sample data for Employees table
INSERT INTO Employees (EmployeeID, EmployeeName, DepartmentID, Salary)
VALUES
    (1, 'John Doe', 1, 50000.00),
    (2, 'Jane Smith', 2, 60000.00),
    (3, 'Michael Johnson', 1, 55000.00),
    (4, 'Emily Brown', 2, 58000.00),
    (5, 'David Lee', 1, 50000.00),
    (6, 'Sarah Clark', 3, 62000.00),
    (7, 'James Wilson', 1, 55000.00);

-- Table for student scores
CREATE TABLE StudentScores (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(100),
    ExamScore INT
);

-- Sample data for StudentScores table
INSERT INTO StudentScores (StudentID, StudentName, ExamScore)
VALUES
    (1, 'Alice Johnson', 85),
    (2, 'Bob Smith', 92),
    (3, 'Charlie Brown', 78),
    (4, 'Diana Lee', 85),
    (5, 'Eva Wilson', 70),
    (6, 'Frank Clark', 92),
    (7, 'Gina Miller', 78),
    (8, 'Henry Davis', 85);

-- Table for sales data
CREATE TABLE Sales (
    SaleID INT PRIMARY KEY,
    SaleDate DATE,
    Revenue DECIMAL(12, 2)
);

-- Sample data for Sales table
INSERT INTO Sales (SaleID, SaleDate, Revenue)
VALUES
    (1, '2023-01-05', 15000.00),
    (2, '2023-01-15', 12000.00),
    (3, '2023-02-08', 18000.00),
    (4, '2023-02-20', 20000.00),
    (5, '2023-03-10', 25000.00),
    (6, '2023-03-25', 22000.00),
    (7, '2023-04-12', 19000.00),
    (8, '2023-04-28', 21000.00);



-- Example RAnking Functions


    
SELECT EmployeeID, EmployeeName, DepartmentID, Salary,       
       ROW_NUMBER() OVER (ORDER BY DepartmentID) AS RowNumber
FROM Employees;



    
SELECT EmployeeID, EmployeeName, DepartmentID, Salary,       
       RANK() OVER (ORDER BY DepartmentID) AS RankNumber
FROM Employees;


SELECT 
    EmployeeID, Salary,
    DENSE_RANK() OVER (ORDER BY Salary DESC) AS dense_ranking,
    ROW_NUMBER() OVER (ORDER BY Salary DESC) AS row_numbering
FROM 
    Employees;



-- RANK(): This function assigns a rank to each row based on the specified order. Rows with the same values receive the same rank, and the next rank is skipped accordingly.





-- Ranking with Ties: Write a query to rank employees by their salaries in descending order, where employees with the same salary receive the same rank, and the next rank is skipped.



    
SELECT EmployeeName,
       RANK() OVER (ORDER BY salary DESC) AS RankNumber
FROM Employees;





-- Dense Ranking: Create a query to produce a dense rank for students based on their exam scores in ascending order, ensuring no ranks are skipped.

    
SELECT StudentName,
       DENSE_RANK() OVER (ORDER BY ExamScore) AS RankNumber
FROM StudentScores;

-- Top N per Group: Write a query to find the top 3 highest-paid employees within each department.

WITH RankedEmployees AS (
    SELECT EmployeeName, 
           Salary,
           DepartmentID,
           ROW_NUMBER() OVER (PARTITION BY DepartmentID ORDER BY Salary DESC) AS RankNumber
      FROM Employees
)


SELECT EmployeeName, 
       Salary,
       DepartmentID
FROM RankedEmployees
WHERE RankNumber <= 3;



-- Percentile Ranking: Calculate the percentile rank of each student based on their exam scores, considering ties.

SELECT
  StudentName,
  PERCENT_RANK() OVER (ORDER BY ExamScore)
FROM
  StudentScores;




-- Running Total Rank: Create a query to calculate a running total rank of sales revenue by month, resetting the rank at the beginning of each new month.

SELECT Revenue
	FROM Sales;

SELECT
  SaleID,
  SaleDate,
  ROW_NUMBER() OVER (PARTITION BY YEAR(SaleDate), MONTH(SaleDate) ORDER BY Revenue DESC) AS RankNumber
FROM
  Sales;

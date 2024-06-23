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

CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY,
    ProjectName VARCHAR(100),
    DepartmentID INT
);

CREATE TABLE EmployeeProjects (
    EmployeeID INT,
    ProjectID INT,
    PRIMARY KEY (EmployeeID, ProjectID)
);

INSERT INTO Employees (EmployeeID, EmployeeName, Salary, DepartmentID) VALUES
(1, 'Alice', 60000, 1),
(2, 'Bob', 70000, 2),
(3, 'Charlie', 50000, 1),
(4, 'David', 80000, 3),
(5, 'Eve', 90000, NULL);

INSERT INTO Departments (DepartmentID, DepartmentName) VALUES
(1, 'HR'),
(2, 'Engineering'),
(3, 'Sales');

INSERT INTO Projects (ProjectID, ProjectName, DepartmentID) VALUES
(1, 'Project A', 1),
(2, 'Project B', 2),
(3, 'Project C', 3),
(4, 'Project D', NULL);

INSERT INTO EmployeeProjects (EmployeeID, ProjectID) VALUES
(1, 1),
(1, 2),
(2, 2),
(3, 1),
(4, 3);








-- ### Practice Questions

-- 1. **List Employees and their Departments:**
--    Write a query to list all employees along with their respective department names. Include employees who do not belong to any department.

SELECT
  EmployeeName,
  DepartmentName
FROM Employees
LEFT JOIN Departments
ON Employees.DepartmentID = Departments.DepartmentID;








-- 2. **Employees and Projects:**
--    Write a query to list all employees and the projects they are working on. Include employees who are not assigned to any projects and projects that have no employees assigned to them.



SELECT
  EmployeeName,
  COALESCE(ProjectName, 'No Project') AS ProjectName
FROM Employees e
LEFT JOIN EmployeeProjects ep
ON e.EmployeeID = ep.EmployeeID
LEFT JOIN Projects p
ON ep.ProjectID = p.ProjectID

 UNION

SELECT
  COALESCE(EmployeeName, 'No Employee') AS EmployeeName,
  ProjectName
FROM Employees e
LEFT JOIN EmployeeProjects ep
ON e.EmployeeID = ep.EmployeeID
RIGHT JOIN Projects p
ON ep.ProjectID = p.ProjectID;







-- 3. **Departments and their Projects:**
--    Write a query to list all departments along with the projects under them. Include departments that have no projects and projects that are not assigned to any department.


SELECT
  DepartmentName,
  ProjectName
  FROM Departments d
       LEFT JOIN Projects p
	   ON d.DepartmentID = p.DepartmentID
	      
UNION
  
SELECT
  DepartmentName,
  ProjectName
  FROM Departments d
       RIGHT JOIN Projects p
	   ON d.DepartmentID = p.DepartmentID;
	      











-- 4. **Employees and their Project Departments:**
--    Write a query to list all employees along with the departments of the projects they are working on. Include employees working on projects that are not assigned to any department and employees who are not working on any projects.

-- 5. **Highest Salary by Department:**
--    Write a query to find the highest salary in each department. Include departments that have no employees and indicate that they have no salaries.

-- These questions will help you practice different types of joins, including inner joins, left joins, right joins, and full outer joins (if supported by your SQL environment).

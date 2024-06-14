DROP DATABASE IF EXISTS test_db;
		CREATE DATABASE test_db;

USE test_db;

CREATE TABLE employees (
  employee_id INT PRIMARY KEY AUTO_INCREMENT,
  salary DECIMAL(10, 2),
  employee_name VARCHAR(100),
  department_id INT
);

INSERT INTO employees(salary, employee_name, department_id)
VALUES
(1000, 'Alice', 1),
(1200, 'Bob', 1),
(800, 'Charlie', 2),
(1500, 'David', 2),
(2000, 'Eve', 3),
(1800, 'Frank', 3),
(700, 'Grace', 1);

SELECT e.employee_id, e.employee_name, e.salary, e.department_id
FROM employees e
WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department_id = e.department_id
);

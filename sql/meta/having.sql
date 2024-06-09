DROP DATABASE IF EXISTS sales_db;
CREATE DATABASE sales_db;
USE sales_db;

CREATE TABLE employees(
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100),
  department VARCHAR(100)
);

INSERT INTO employees(name, department)
VALUES
  ('John Doe', 'HR'),
  ('Jane Doe', 'HR'),
  ('Alice', 'IT'),
  ('Bob', 'IT'),
  ('Charlie', 'IT'),
  ('David', 'HR'),
  ('Eve', 'HR'),
  ('Frank', 'IT'),
  ('Grace', 'IT'),
  ('Heidi', 'HR'),
  ('Ivan', 'HR'),
  ('Judy', 'IT'),
  ('Kevin', 'IT'),
  ('Linda', 'HR'),
  ('Mary', 'HR'),
  ('Nancy', 'IT'),
  ('Oscar', 'IT'),
  ('Pam', 'HR'),
  ('Quincy', 'HR'),
  ('Randy', 'IT'),
  ('Steve', 'IT'),
  ('Tina', 'HR'),
  ('Ursula', 'HR'),
  ('Victor', 'IT'),
  ('Wendy', 'IT'),
  ('Xavier', 'HR'),
  ('Yvonne', 'HR'),
  ('Zack', 'IT'),
  ('Amy', 'IT'),
  ('Ben', 'HR'),
  ('Cathy', 'HR'),
  ('Dan', 'IT'),
  ('Eva', 'IT'),
  ('Felix', 'HR'),
  ('Gina', 'HR'),
  ('Hank', 'IT'),
  ('Iris', 'IT'),
  ('Jack', 'HR'),
  ('Kathy', 'HR'),
  ('Lenny', 'IT'),
  ('Mona', 'IT'),
  ('Ned', 'HR'),
  ('Olive', 'HR'),
  ('Pete', 'IT'),
  ('Quinn', 'IT'),
  ('Rita', 'HR'),
  ('Sam', 'HR'),
  ('Tom', 'IT'),
  ('Uma', 'IT'),
  ('Vince', 'HR'),
  ('Wanda', 'HR'),
  ('Xander', 'IT'),
  ('Yara', 'IT'),
  ('Zoe', 'HR');

SELECT department, COUNT(*) as num_employees 
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;

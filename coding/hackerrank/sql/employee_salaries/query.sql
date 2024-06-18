CREATE DATABASE IF NOT EXISTS TestDB;

USE TestDB;

DROP TABLE IF EXISTS employee;

CREATE TABLE employee (
  employee_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(21) NOT NULL,
  months INTEGER NOT NULL,
  salary INTEGER NOT NULL
);

INSERT INTO employee (name, months, salary) VALUES
('Tom', 1, 199),
('Ed', 1, 199),
('Ed', 1, 188),
('Tom', 1, 199),
('William', 1, 100);


SELECT name
FROM employee
WHERE salary > 2000
	AND months < 10;



DROP DATABASE TestDB;

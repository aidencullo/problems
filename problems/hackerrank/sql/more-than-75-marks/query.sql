-- Setup the database
CREATE DATABASE IF NOT EXISTS TestDB;

USE TestDB;

DROP TABLE IF EXISTS students;

CREATE TABLE students (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(21) NOT NULL,
  marks INTEGER NOT NULL
);

-- Insert data
INSERT INTO students (name, marks) VALUES
('Wilz', 100),
('William', 101),
('William', 99),
('Wilz', 100),
('Dave', 100),
('John', 50),
('John', 50),
('Ed', 76),
('William', 100);


SELECT name
FROM students
WHERE marks > 75
ORDER BY 
    SUBSTRING(name, -3),
    id;


-- select Name from Students where Marks > 75 order by substring(Ucase(Name), -3) asc, id asc;


-- Cleanup
-- drop the database
DROP DATABASE TestDB;

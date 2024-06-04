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


-- Actual query
SELECT *
FROM students
WHERE marks > 75
ORDER BY 
    SUBSTRING(name, LENGTH(name) - 2, 3),
    id;



-- Cleanup
-- drop the database
DROP DATABASE TestDB;

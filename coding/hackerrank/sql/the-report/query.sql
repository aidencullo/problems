CREATE DATABASE IF NOT EXISTS TestDB;

USE TestDB;

DROP TABLE IF EXISTS CITY;
DROP TABLE IF EXISTS COUNTRY;


-- Create the Students table
CREATE TABLE Students (
    ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Marks INT
);

-- Create the Grades table
CREATE TABLE Grades (
    ID INT PRIMARY KEY,
    Grade INT
);

-- Insert sample data into the Students table
INSERT INTO Students (ID, Name, Marks) VALUES
(1, 'Maria', 99),
(2, 'Jane', 81),
(3, 'Julia', 88),
(4, 'Scarlet', 78),
(5, 'Lara', 72),
(6, 'John', 63),
(7, 'Eve', 69);

-- Insert sample data into the Grades table
INSERT INTO Grades (ID, Grade) VALUES
(1, 10),
(2, 9),
(3, 9),
(4, 8),
(5, 7),
(6, 7),
(7, 6);

SELECT
*
FROM
Students
JOIN

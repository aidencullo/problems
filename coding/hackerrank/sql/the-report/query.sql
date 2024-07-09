DROP DATABASE IF EXISTS School;
CREATE DATABASE School;
USE School;

-- Create the Students table
CREATE TABLE Students (
    ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Marks INT
);

-- Create the Grades table
CREATE TABLE Grades (
    Grade INT,
    Min_Mark INT,
    Max_Mark INT
);

-- Insert sample data into Students table
INSERT INTO Students (ID, Name, Marks) VALUES
(1, 'Julia', 88),
(2, 'Scarlet', 78),
(3, 'Jane', 81),
(4, 'Maria', 99),
(5, 'Tom', 63),
(6, 'Jerry', 68);

-- Insert sample data into Grades table
INSERT INTO Grades (Grade, Min_Mark, Max_Mark) VALUES
(10, 90, 100),
(9, 80, 89),
(8, 70, 79),
(7, 60, 69),
(6, 50, 59),
(5, 40, 49),
(4, 30, 39),
(3, 20, 29),
(2, 10, 19),
(1, 0, 9);

SELECT
IF (grade < 8, NULL, name),
grade,
marks
FROM
(SELECT
name,
(SELECT grade FROM grades WHERE min_mark <= marks AND max_mark >= marks) AS grade,
marks
FROM
Students
ORDER BY
grade DESC,
name) AS s

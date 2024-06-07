DROP DATABASE IF EXISTS SampleDB;
CREATE DATABASE SampleDB;

USE SampleDB;

CREATE TABLE triangles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    A INT,
    B INT,
    C INT
);


INSERT INTO triangles(A, B, C) VALUES
(1, 2, 3),
(4, 5, 6),
(7, 8, 9);


SELECT
IF(A + B + C <= GREATEST(A, B, C) * 2, 'Not A Triangle',
IF(A = B AND B = C, 'Equilateral',
IF(A = B OR B = C OR A = C, 'Isosceles', 'Scalene')))
FROM 
    triangles;

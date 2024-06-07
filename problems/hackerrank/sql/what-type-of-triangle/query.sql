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
    CASE
        WHEN A + B + C <= GREATEST(A, B, C) * 2 THEN 'Not A Triangle'
        WHEN A=B AND B=C THEN 'Equilateral'
        WHEN A=B OR B=C OR A=C THEN 'Isosceles'
        ELSE 'Scalene'
    END AS triangle_type
FROM 
    triangles;

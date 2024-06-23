DROP DATABASE IF EXISTS SampleDB;
		CREATE DATABASE SampleDB;

USE SampleDB;

-- Drop the OCCUPATIONS table if it exists (optional for reset)
DROP TABLE IF EXISTS OCCUPATIONS;

-- Create the OCCUPATIONS table
CREATE TABLE OCCUPATIONS (
    Name VARCHAR(50),
    Occupation VARCHAR(20)
);

-- Insert sample data into OCCUPATIONS
INSERT INTO OCCUPATIONS (Name, Occupation) VALUES
('Jenny', 'Doctor'),
('Samantha', 'Doctor'),
('Ashley', 'Professor'),
('Christeen', 'Professor'),
('Meera', 'Singer'),
('Priya', 'Singer'),
('Jane', 'Actor'),
('Julia', 'Actor'),
('Ketty', 'Professor'),
  ('Maria', 'Singer');

-- Query to pivot the OCCUPATIONS table
SELECT
    MAX(CASE WHEN Occupation = 'Doctor' THEN Name ELSE NULL END) AS Doctor,
    MAX(CASE WHEN Occupation = 'Professor' THEN Name ELSE NULL END) AS Professor,
    MAX(CASE WHEN Occupation = 'Singer' THEN Name ELSE NULL END) AS Singer,
    MAX(CASE WHEN Occupation = 'Actor' THEN Name ELSE NULL END) AS Actor
FROM
    OCCUPATIONS
GROUP BY
    Name
ORDER BY
    Name;

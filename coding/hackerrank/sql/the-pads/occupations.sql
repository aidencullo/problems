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



SELECT
  Name
FROM
    OCCUPATIONS
GROUP BY
    Name
ORDER BY
    Name;

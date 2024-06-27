DROP DATABASE IF EXISTS pivot;
		CREATE DATABASE pivot;

		USE pivot;


-- Step 1: Create the Sales table
CREATE TABLE IF NOT EXISTS OCCUPATIONS (
  Name VARCHAR(255),
  Occupation VARCHAR(255)
);

-- Step 2: Insert sample data into the Sales table
INSERT INTO OCCUPATIONS (Name, Occupation) VALUES
('Samantha', 'Doctor'),
('Julia', 'Actor'),
('Maria', 'Actor'),
('Meera', 'Singer'),
('Ashley', 'Professor'),
('Ketty', 'Professor'),
('Christeen', 'Professor'),
('Jane', 'Actor'),
('Jenny', 'Doctor'),
('Priya', 'Singer');


SELECT 
    MIN(CASE WHEN Occupation = 'Doctor' THEN Name END) AS Doctor,
    MAX(CASE WHEN Occupation = 'Professor' THEN Name END) AS Professor,
    MAX(CASE WHEN Occupation = 'Singer' THEN Name END) AS Singer,
    MAX(CASE WHEN Occupation = 'Actor' THEN Name END) AS Actor
FROM (
    SELECT Name, Occupation, 
           ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) AS rn
    FROM OCCUPATIONS
) AS ranked
GROUP BY rn;

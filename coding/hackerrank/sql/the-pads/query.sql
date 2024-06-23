DROP DATABASE IF EXISTS SampleDB;
CREATE DATABASE SampleDB;

USE SampleDB;

CREATE TABLE OCCUPATIONS (
    name VARCHAR(255),
    Occupation VARCHAR(50)
);

INSERT INTO OCCUPATIONS (name, Occupation) VALUES
('Ashely', 'Professor'),
('Christeen', 'Professor'),
('Jane', 'Actor'),
('Jenny', 'Doctor'),
('Julia', 'Actor'),
('Ketty', 'Professor'),
('Maria', 'Actor'),
('Meera', 'Singer'),
('Priya', 'Singer'),
('Samantha', 'Doctor');


-- Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first letter of each profession as a parenthetical (i.e.: enclosed in parentheses). For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).
-- Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order, and output them in the following format:

SELECT
  CONCAT(name, '(', SUBSTRING(Occupation, 1, 1), ')') AS name_occupation
  FROM OCCUPATIONS
 ORDER BY name;


SELECT
  CONCAT('There are a total of ', COUNT(*), ' ', LOWER(Occupation), 's.') AS occupation_count
  FROM OCCUPATIONS
  GROUP BY Occupation
  ORDER BY COUNT(*) ASC;




-- There are a total of [occupation_count] [occupation]s.
-- where [occupation_count] is the number of occurrences of an occupation in OCCUPATIONS and [occupation] is the lowercase occupation name. If more than one Occupation has the same [occupation_count], they should be ordered alphabetically.

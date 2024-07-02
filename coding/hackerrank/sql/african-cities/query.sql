CREATE DATABASE IF NOT EXISTS TestDB;

USE TestDB;

DROP TABLE IF EXISTS CITY;
DROP TABLE IF EXISTS COUNTRY;


-- Create the CITY table
CREATE TABLE CITY (
    ID INT PRIMARY KEY,
    Name VARCHAR(50),
    CountryCode VARCHAR(3),
    District VARCHAR(50),
    Population INT
);

-- Create the COUNTRY table
CREATE TABLE COUNTRY (
    Code VARCHAR(3) PRIMARY KEY,
    Name VARCHAR(50),
    Continent VARCHAR(50),
    Region VARCHAR(50),
    SurfaceArea FLOAT,
    Population INT,
    LifeExpectancy FLOAT,
    GNP FLOAT,
    HeadOfState VARCHAR(50),
    Capital VARCHAR(50),
    Code2 VARCHAR(2)
);

-- Insert sample data into the CITY table
INSERT INTO CITY (ID, Name, CountryCode, District, Population) VALUES
(1, 'Tokyo', 'JPN', 'Tokyo', 13929286),
(2, 'Jakarta', 'IDN', 'Jakarta', 10075307),
(3, 'Seoul', 'KOR', 'Seoul', 10349312),
(4, 'Mumbai', 'IND', 'Maharashtra', 12442373),
(5, 'Shanghai', 'CHN', 'Shanghai', 24150000);

-- Insert sample data into the COUNTRY table
INSERT INTO COUNTRY (Code, Name, Continent, Region, SurfaceArea, Population, LifeExpectancy, GNP, HeadOfState, Capital, Code2) VALUES
('JPN', 'Japan', 'Asia', 'Eastern Asia', 377835, 126851000, 84.63, 5152350, 'Fumio Kishida', 'Tokyo', 'JP'),
('IDN', 'Indonesia', 'Asia', 'South-Eastern Asia', 1904569, 273523615, 71.84, 1197260, 'Joko Widodo', 'Jakarta', 'ID'),
('KOR', 'South Korea', 'Asia', 'Eastern Asia', 100032, 51780579, 82.88, 1803830, 'Yoon Suk-yeol', 'Seoul', 'KR'),
('IND', 'India', 'Asia', 'Southern Asia', 3287263, 1393409038, 69.66, 2875140, 'Droupadi Murmu', 'New Delhi', 'IN'),
('CHN', 'China', 'Asia', 'Eastern Asia', 9596961, 1402112000, 76.91, 15362000, 'Xi Jinping', 'Beijing', 'CN');

-- Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.

-- Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

SELECT
CITY.Name
FROM
CITY
JOIN
COUNTRY
ON
CITY.CountryCode = COUNTRY.Code
WHERE CONTINENT = 'Africa'

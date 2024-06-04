-- Setup the database
CREATE DATABASE IF NOT EXISTS TestDB;

USE TestDB;

DROP TABLE IF EXISTS station;

CREATE TABLE station (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  city VARCHAR(21) NOT NULL,
  state VARCHAR(2),
  lat_n INTEGER,
  long_n INTEGER
);

-- Insert data
INSERT INTO station (city) VALUES
('John'),
('Dave'),
('Abe'),
('Michael'),
('William');




-- Actual query
SELECT DISTINCT city
FROM station
WHERE LOWER(city) LIKE '%a'
OR LOWER(city) LIKE '%e'
OR LOWER(city) LIKE '%i'
OR LOWER(city) LIKE '%o'
OR LOWER(city) LIKE '%u';





-- Cleanup
-- drop the database
DROP DATABASE TestDB;

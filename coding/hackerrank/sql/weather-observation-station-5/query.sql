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
('Michael'),
('William');




-- Actual query
SELECT city, (SELECT MIN(LENGTH(city)) FROM station) AS min_length
FROM station
ORDER BY LENGTH(city), city ASC
LIMIT 1;

SELECT city, (SELECT MAX(LENGTH(city)) FROM station) AS min_length
FROM station
ORDER BY LENGTH(city) DESC, city ASC
LIMIT 1;




-- Cleanup
-- drop the database
DROP DATABASE TestDB;

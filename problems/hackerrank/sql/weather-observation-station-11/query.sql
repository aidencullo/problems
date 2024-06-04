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
SELECT DISTINCT city FROM station
WHERE city RLIKE '^[^aeiou]|[^aeiou]$';




-- Cleanup
-- drop the database
DROP DATABASE TestDB;

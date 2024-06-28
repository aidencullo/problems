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

INSERT INTO station (city) VALUES
('John'),
('John'),
('William');
	
SELECT
ROUND(SUM(lat_n), 2) AS lat_n,
ROUND(SUM(long_w), 2) AS long_n
FROM station;


-- SELECT
-- ROUND(SUM(lat_n), 2) AS lat_n,
-- ROUND(SUM(long_w), 2) AS long_n
-- FROm station;

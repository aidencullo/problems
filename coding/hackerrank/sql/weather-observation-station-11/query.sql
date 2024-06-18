CREATE DATABASE IF
NOT EXISTS TestDB;

USE TestDB;

DROP TABLE
IF EXISTS station;

CREATE TABLE station (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  city VARCHAR(21) NOT NULL,
  state VARCHAR(2),
  lat_n INTEGER,
  long_n INTEGER
);

INSERT INTO station (city) VALUES
('John'),
('Dave'),
('Abe'),
('Michael'),
('William');



SELECT DISTINCT city
FROM station
WHERE city RLIKE '^[^aeiou]|[^aeiou]$';


DROP DATABASE TestDB;

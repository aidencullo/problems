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
ROUND(MAX(lat_n), 4) AS lat_n
FROM
station
WHERE
lat_n < 137.2345

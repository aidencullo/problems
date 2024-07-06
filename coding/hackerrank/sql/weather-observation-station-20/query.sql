CREATE DATABASE IF NOT EXISTS TestDB;

USE TestDB;

DROP TABLE IF EXISTS station;


-- Create the STATION table
CREATE TABLE STATION (
    ID INT PRIMARY KEY,
    CITY VARCHAR(50),
    STATE VARCHAR(50),
    LAT_N FLOAT,
    LONG_W FLOAT
);

-- Insert sample data into the STATION table
INSERT INTO STATION (ID, CITY, STATE, LAT_N, LONG_W) VALUES
(1, 'San Francisco', 'California', 37.7749, -122.4194),
(2, 'Los Angeles', 'California', 34.0522, -118.2437),
(3, 'New York', 'New York', 40.7128, -74.0060),
(4, 'Chicago', 'Illinois', 41.8781, -87.6298),
(5, 'Houston', 'Texas', 29.7604, -95.3698),
(6, 'Phoenix', 'Arizona', 33.4484, -112.0740),
(7, 'Philadelphia', 'Pennsylvania', 39.9526, -75.1652),
(8, 'San Antonio', 'Texas', 29.4241, -98.4936),
(9, 'San Diego', 'California', 32.7157, -117.1611),
(10, 'Dallas', 'Texas', 32.7767, -96.7970);

SELECT
ROUND(AVG(lat_n), 4)
FROM
(
SELECT
lat_n,
ROW_NUMBER() OVER(ORDER BY lat_n) AS bb
FROM
STATION
) b
WHERE
b.bb = (SELECT FLOOR((COUNT(*) + 1) / 2) FROM STATION)
OR
b.bb = (SELECT CEIL((COUNT(*) + 1) / 2) FROM STATION);

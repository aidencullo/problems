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
(5, 'Houston', 'Texas', 29.7604, -95.3698);

SELECT
ROUND(
SQRT(POW(MAX(lat_n) - MIN(lat_n), 2) + POW(MAX(long_w) - MIN(long_w), 2))
, 4)
FROM
station

DROP DATABASE IF EXISTS company;
CREATE DATABASE company;
USE company;



-- Create the Neighborhoods table
CREATE TABLE neighborhoods (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    city_id INTEGER NOT NULL
);

-- Create the Users table
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    neighborhood_id INTEGER,
    created_at DATETIME NOT NULL,
    FOREIGN KEY (neighborhood_id) REFERENCES neighborhoods(id)
);

-- Insert sample data into Neighborhoods
INSERT INTO neighborhoods (id, name, city_id) VALUES
(1, 'Downtown', 101),
(2, 'Uptown', 101),
(3, 'Suburbia', 102),
(4, 'Riverside', 103),
(5, 'Lakeside', 104);

-- Insert sample data into Users
INSERT INTO users (id, name, neighborhood_id, created_at) VALUES
(1, 'Alice Johnson', 1, '2024-01-15 08:30:00'),
(2, 'Bob Smith', 1, '2024-02-20 09:45:00'),
(3, 'Charlie Brown', 2, '2024-03-10 10:00:00'),
(4, 'David Wilson', 3, '2024-04-25 14:15:00'),
(5, 'Eva Green', 4, '2024-05-30 11:00:00'),
(6, 'Frank Moore', 5, '2024-06-05 12:30:00'),
(7, 'Grace Lee', 2, '2024-07-20 16:45:00'),
(8, 'Henry Adams', 3, '2024-08-10 13:00:00'),
(9, 'Ivy Clark', 1, '2024-09-15 17:00:00'),
(10, 'Jack Martinez', 4, '2024-10-05 18:30:00');


SELECT
    neighborhoods.name AS neighborhood_name,
    COUNT(users.id) AS user_count
FROM
    neighborhoods
LEFT JOIN users ON neighborhoods.id = users.neighborhood_id
GROUP BY
    neighborhoods.name
HAVING
    COUNT(users.id) = 0

 -- Write a SQL query to create a histogram of the number of comments per user in January 2020. Assume bin buckets class intervals of one.

DROP DATABASE IF EXISTS company;
CREATE DATABASE company;
USE company;

CREATE TABLE users(
id INT PRIMARY KEY AUTO_INCREMENT,
name TEXT,
created_at DATE,
neighborhood_id INT,
date DATETIME,
mail TEXT
);

CREATE TABLE comments(
id INT PRIMARY KEY AUTO_INCREMENT,
user_id INT,
body VARCHAR(255),
created_at DATETIME
);

-- Insert sample data into users table
INSERT INTO users (name, created_at, neighborhood_id, mail) VALUES
('Alice', '2019-12-15 08:30:00', 1, 'alice@example.com'),
('Bob', '2019-11-20 09:00:00', 2, 'bob@example.com'),
('Carol', '2020-01-05 10:00:00', 3, 'carol@example.com');

-- Insert sample data into comments table
INSERT INTO comments (user_id, body, created_at) VALUES
(1, 'Great post!', '2020-01-10 08:30:00'),
(1, 'Thanks for sharing!', '2020-01-15 09:00:00'),
(2, 'Interesting read.', '2020-01-20 10:00:00'),
(2, 'I agree!', '2020-01-21 11:00:00'),
(3, 'Nice article.', '2020-01-07 12:00:00'),
(3, 'Well written.', '2020-01-08 13:00:00'),
(3, 'Enjoyed reading this.', '2020-01-09 14:00:00');

WITH user_comments AS (
SELECT
c.user_id,
COUNT(*) AS comment_count
FROM
comments c
WHERE
MONTH(c.created_at) = 1
AND
YEAR(c.created_at) = 2020
GROUP BY
c.user_id
)

SELECT
comment_count,
COUNT(*) AS freq
FROM
user_comments u
GROUP BY
comment_count

























DROP DATABASE IF EXISTS company;
CREATE DATABASE company;
USE company;



-- Create the friends table
CREATE TABLE friends (
    user_id INTEGER,
    friend_id INTEGER
);

-- Create the page_likes table
CREATE TABLE page_likes (
    user_id INTEGER,
    page_id INTEGER
);

-- Insert sample data into the friends table
INSERT INTO friends (user_id, friend_id) VALUES
(1, 2),
(1, 3),
(2, 3),
(2, 4),
(3, 4),
(3, 5),
(4, 5);

-- Insert sample data into the page_likes table
INSERT INTO page_likes (user_id, page_id) VALUES
(1, 101),
(1, 102),
(2, 101),
(2, 103),
(3, 101),
(3, 103),
(3, 104),
(4, 105),
(5, 106);

WITH friend_likes AS (
    SELECT
	f.user_id,
	f.friend_id,
	p.page_id
    FROM
	friends f
    JOIN
	page_likes p
    ON
	f.friend_id = p.user_id
)

SELECT DISTINCT
page_id
FROM friend_likes
WHERE
page_id NOT IN (
    SELECT
	page_id
    FROM page_likes
    WHERE
	friend_likes.user_id = page_likes.user_id
)
AND
user_id = 1;

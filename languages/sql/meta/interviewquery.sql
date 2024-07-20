 -- Write a SQL query to create a histogram of the number of comments per user in January 2020. Assume bin buckets class intervals of one.

DROP DATABASE IF EXISTS company;
CREATE DATABASE company;
USE company;


-- Create the 'events' table
CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    user_id INTEGER NOT NULL,
    created_at DATETIME NOT NULL,
    action VARCHAR(20) NOT NULL,
    url VARCHAR(255),
    platform VARCHAR(255)
);

-- Insert sample data into the 'events' table
INSERT INTO events (user_id, created_at, action, url, platform)
VALUES
    (123, '2020-01-01 08:30:00', 'post_enter', 'http://example.com/post1', 'web'),
    (123, '2020-01-01 09:00:00', 'post_submit', 'http://example.com/post1', 'web'),
    (456, '2020-01-02 10:00:00', 'post_enter', 'http://example.com/post2', 'mobile'),
    (456, '2020-01-02 10:30:00', 'post_canceled', 'http://example.com/post2', 'mobile'),
    (789, '2020-01-03 11:00:00', 'post_enter', 'http://example.com/post3', 'web'),
    (789, '2020-01-03 11:15:00', 'post_submit', 'http://example.com/post3', 'web');

SELECT
    AVG(CASE
    WHEN action = 'post_submit' THEN 1
    WHEN action = 'post_canceled' THEN 0
    END)
FROM
events

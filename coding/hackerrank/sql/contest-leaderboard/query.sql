DROP DATABASE IF EXISTS HackerRank;
CREATE DATABASE HackerRank;
USE HackerRank;

-- Drop the tables if they already exist
DROP TABLE IF EXISTS Submissions;
DROP TABLE IF EXISTS Hackers;

-- Create the Hackers table
CREATE TABLE Hackers (
    hacker_id INT PRIMARY KEY,
    name VARCHAR(100)
);

-- Create the Submissions table
CREATE TABLE Submissions (
    submission_id INT PRIMARY KEY,
    hacker_id INT,
    challenge_id INT,
    score INT,
    FOREIGN KEY (hacker_id) REFERENCES Hackers(hacker_id)
);

-- Insert data into the Hackers table
INSERT INTO Hackers (hacker_id, name) VALUES 
(4071, 'Rose'),
(74842, 'Lisa'),
(84072, 'Bonnie'),
(4806, 'Angela'),
(26071, 'Frank'),
(80305, 'Kimberly'),
(49438, 'Patrick');

-- Insert data into the Submissions table
INSERT INTO Submissions (submission_id, hacker_id, challenge_id, score) VALUES 
(1, 4071, 19797, 100),
(2, 4071, 49593, 91),
(3, 74842, 19797, 90),
(4, 74842, 63132, 84),
(5, 84072, 49593, 100),
(6, 84072, 63132, 10),
(7, 4806, 49593, 89),
(8, 26071, 19797, 85),
(9, 80305, 19797, 67),
(10, 49438, 19797, 43),
(11, 49438, 19797, 100);


-- SELECT
-- hacker_id,
-- challenge_id,
-- COUNT(*) AS total_submissions,
-- MAX(score) AS max_score
-- FROM
-- Submissions
-- GROUP BY
-- hacker_id, challenge_id;

WITH sub AS (
    SELECT
        hacker_id,
        challenge_id,
        MAX(score) AS max_score
    FROM
        submissions
    GROUP BY
        hacker_id, challenge_id
)
SELECT
    h.hacker_id,
    h.name,
    SUM(s.max_score) AS max_score
FROM
    hackers h
JOIN
    sub s ON h.hacker_id = s.hacker_id
GROUP BY
    h.hacker_id
HAVING
    SUM(s.max_score) > 0
ORDER BY
    SUM(s.max_score) DESC,
    h.hacker_id ASC;


WITH CTE AS (SELECT h.hacker_id, h.name, s.challenge_id, s.score,
    ROW_NUMBER () OVER (
        PARTITION BY h.hacker_id, s.challenge_id
        ORDER BY s.score DESC
    ) challenge_rank
FROM hackers h JOIN Submissions s ON h.hacker_id = s.hacker_id)

SELECT hacker_id, name, SUM(score) 
FROM CTE 
WHERE challenge_rank = 1 
GROUP BY hacker_id, name 
HAVING SUM(score) > 0 
ORDER BY SUM(score) DESC, hacker_id;

SELECT *
FROM (
    SELECT 
        h.hacker_id, 
        h.name, 
        SUM(t.score) AS score
    FROM 
        Hackers h
    INNER JOIN (
        SELECT 
            s.hacker_id, 
            s.challenge_id, 
            MAX(s.score) AS score
        FROM 
            Submissions s
        GROUP BY 
            s.hacker_id, 
            s.challenge_id
    ) t ON t.hacker_id = h.hacker_id
    GROUP BY 
        h.hacker_id
) q
WHERE 
    q.score > 0
ORDER BY 
    q.score DESC, 
    q.hacker_id;

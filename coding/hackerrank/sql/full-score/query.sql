-- Julia just finished conducting a coding contest, and she needs your help assembling the leaderboard! Write a query to print the respective hacker_id and name of hackers who achieved full scores for more than one challenge. Order your output in descending order by the total number of challenges in which the hacker earned a full score. If more than one hacker received full scores in same number of challenges, then sort them by ascending hacker_id.

DROP DATABASE IF EXISTS Hackers;
CREATE DATABASE Hackers;

USE Hackers;

-- Create Hackers table
CREATE TABLE Hackers (
    hacker_id INT PRIMARY KEY,
    name VARCHAR(50)
);

-- Create Difficulty table
CREATE TABLE Difficulty (
    difficulty_level INT PRIMARY KEY,
    score INT
);

-- Create Challenges table
CREATE TABLE Challenges (
    challenge_id INT PRIMARY KEY,
    hacker_id INT,
    difficulty_level INT,
    FOREIGN KEY (hacker_id) REFERENCES Hackers(hacker_id),
    FOREIGN KEY (difficulty_level) REFERENCES Difficulty(difficulty_level)
);

-- Create Submissions table
CREATE TABLE Submissions (
    submission_id INT PRIMARY KEY,
    hacker_id INT,
    challenge_id INT,
    score INT,
    FOREIGN KEY (hacker_id) REFERENCES Hackers(hacker_id),
    FOREIGN KEY (challenge_id) REFERENCES Challenges(challenge_id)
);

-- Insert sample data into Hackers table
INSERT INTO Hackers (hacker_id, name) VALUES
(86870, 'Alice'),
(90411, 'Joe'),
(12345, 'Bob'),
(67890, 'Charlie'),
(54321, 'David');

-- Insert sample data into Difficulty table
INSERT INTO Difficulty (difficulty_level, score) VALUES
(1, 10),
(2, 30),
(3, 50),
(4, 70),
(5, 90),
(6, 100);

-- Insert sample data into Challenges table
INSERT INTO Challenges (challenge_id, hacker_id, difficulty_level) VALUES
(71055, 86870, 2),
(66730, 90411, 6),
(12356, 12345, 4),
(23467, 67890, 3),
(34578, 54321, 5);

-- Insert sample data into Submissions table
INSERT INTO Submissions (submission_id, hacker_id, challenge_id, score) VALUES
(1, 86870, 71055, 30),
(2, 90411, 71055, 30),
(3, 90411, 66730, 100),
(4, 12345, 12356, 70),
(5, 67890, 23467, 50),
(6, 54321, 34578, 90),
(7, 90411, 34578, 90),
(8, 12345, 71055, 30),
(9, 12345, 66730, 100),
(10, 67890, 66730, 100),
(11, 54321, 12356, 70),
(12, 54321, 23467, 50);

-- SELECT
-- h.hacker_id,
-- h.name
-- FROM
-- (
-- SELECT
-- s.hacker_id
-- FROM
-- Submissions s
-- JOIN
-- Challenges c
-- ON
-- s.challenge_id = c.challenge_id
-- JOIN
-- Difficulty d
-- ON
-- c.difficulty_level = d.difficulty_level
-- JOIN
-- Hackers h
-- ON
-- s.hacker_id = h.hacker_id
-- WHERE
-- d.score = s.score
-- GROUP BY
-- s.hacker_id
-- HAVING
-- COUNT(*) > 1
-- ORDER BY
-- COUNT(*) DESC,
-- s.hacker_id
-- ) AS leaderboard
-- JOIN
-- Hackers h
-- ON
-- leaderboard.hacker_id = h.hacker_id;

WITH full_scores AS (
    SELECT
	s.hacker_id,
	COUNT(*) AS num_full_scores
    FROM
	Submissions s
    JOIN
	Challenges c
    ON
	s.challenge_id = c.challenge_id
    JOIN
	Difficulty d
    ON
	c.difficulty_level = d.difficulty_level
    WHERE
	s.score = d.score
    GROUP BY
	s.hacker_id
    HAVING
        COUNT(*) > 1
)

SELECT
    h.hacker_id,
    h.name
FROM
    full_scores f
JOIN
Hackers h
ON
f.hacker_id = h.hacker_id
ORDER BY
f.num_full_scores DESC,
    h.hacker_id;

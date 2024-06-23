
-- Create the database
DROP DATABASE IF EXISTS school_db;
CREATE DATABASE school_db;

USE school_db;

-- Create the Students table
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(100)
);

-- Create the StudentScores table
CREATE TABLE StudentScores (
    ScoreID INT PRIMARY KEY,
    StudentID INT,
    ExamScore DECIMAL(5, 2),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

-- Insert sample data into Students table
INSERT INTO Students (StudentID, StudentName) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie'),
(4, 'David'),
(5, 'Eve');

-- Insert sample data into StudentScores table
INSERT INTO StudentScores (ScoreID, StudentID, ExamScore) VALUES
(1, 1, 85.5),
(2, 2, 90),
(3, 3, NULL), -- Charlie has not taken an exam
(4, 4, 95),
(5, 5, 70);

SELECT * FROM Students;


-- Question: Write a query to list the names of all students along with their exam scores. Some students may not have taken any exams, in which case they should be labeled as 'No exam taken'.


SELECT
  StudentName,
  COALESCE(ExamScore, 'No exam taken') AS ExamScore
  FROM Students
    JOIN StudentScores
	   ON Students.StudentID = StudentScores.StudentID;

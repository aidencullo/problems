DROP DATABASE IF EXISTS retail_db;
		CREATE DATABASE retail_db;

USE retail_db;

-- setup

-- Create tables
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    best_grade INT,
    best_class VARCHAR(50)
);

CREATE TABLE classes (
    student_id INT,
    class_name VARCHAR(50),
    grade INT,
    PRIMARY KEY (student_id, class_name),
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- Populate students table
INSERT INTO students (id, name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie');

-- Populate classes table
INSERT INTO classes (student_id, class_name, grade) VALUES
(1, 'Math', 95),
(1, 'Science', 95),
(1, 'History', 90),
(2, 'Math', 88),
(2, 'Science', 92),
(2, 'History', 85),
(3, 'Math', 78),
(3, 'Science', 88),
(3, 'History', 88);

-- Display initial data
SELECT 'Initial Students Data:' AS message;
SELECT * FROM students;

SELECT 'Initial Classes Data:' AS message;
SELECT * FROM classes;

-- Update query
UPDATE students s
JOIN (
    SELECT student_id, MAX(grade) as max_grade
    FROM classes
    GROUP BY student_id
) best_grades ON s.id = best_grades.student_id
SET s.best_grade = best_grades.max_grade;
-- JOIN classes c ON s.id = c.student_id AND c.grade = best_grades.max_grade
-- SET s.best_grade = c.grade, s.best_class = c.class_name;

-- Display results
SELECT 'Updated Students Data:' AS message;
SELECT * FROM students;

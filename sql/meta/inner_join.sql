DROP DATABASE school;
CREATE DATABASE IF NOT EXISTS school;

USE school;

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name TEXT
);

CREATE TABLE grades (
  grade_id INT AUTO_INCREMENT PRIMARY KEY,
  student_id INT,
  subject TEXT,
  grade INT
);


INSERT INTO students (name)
VALUES
('Bob'),
('Charlie');

INSERT INTO grades (student_id, subject, grade)
VALUES
(1, 'History', 90),
(10, 'Math', 90),
(2, 'Science', 90),
(3, 'Science', 75);


SELECT *
FROM students
INNER JOIN grades
ON students.student_id = grades.student_id;

-- student_id	name	grade_id	student_id	subject	grade
-- 1	Bob	1	1	History	90
-- 2	Charlie	3	2	Science	90

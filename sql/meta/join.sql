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
('Alice'),
('Bob'),
('Charlie');

INSERT INTO grades (student_id, subject, grade)
VALUES
(1, 'History', 90),
(1, 'Math', 90),
(3, 'Science', 75);

SELECT *
FROM students
LEFT JOIN grades
ON students.student_id = grades.student_id;

-- Expected output
-- 1	Alice	2	1	Math	90
-- 1	Alice	1	1	History	90
-- 2	Bob	NULL	NULL	NULL	NULL
-- 3	Charlie	3	3	Science	75

-- Bob is not in the output because he has no grades. Charlie is in the output because he has a grade in Science. Alice is in the output because she has grades in Math and History.

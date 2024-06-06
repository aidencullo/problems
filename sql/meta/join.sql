DROP DATABASE school;
CREATE DATABASE IF NOT EXISTS school;

USE school;

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name TEXT
);

CREATE TABLE grades (
  grade_id INT AUTO_INCREMENT PRIMARY KEY,
  student_id INTEGER,
  subject TEXT,
  grade INTEGER,
  FOREIGN KEY (student_id) REFERENCES students(student_id)
);

INSERT INTO students (name)
VALUES
('Alice'),
('Bob'),
('Bobby'),
('Charlie');

INSERT INTO grades (student_id, subject, grade)
VALUES
(1, 'Math', 90),
(1, 'Science', 95),
(2, 'Math', 80),
(2, 'Science', 85),
(3, 'Math', 70),
(3, 'Science', 75);

SELECT *
FROM students
LEFT JOIN grades
ON students.student_id = grades.student_id;

DROP DATABASE IF EXISTS retail_db;
		CREATE DATABASE retail_db;

USE retail_db;


-- Create students table
CREATE TABLE students (
  student_id INT PRIMARY KEY,
  student_name VARCHAR(50)
);

-- Create grades table
CREATE TABLE grades (
  student_id INT,
  subject VARCHAR(50),
  grade INT,
  FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- Insert data into students table
INSERT INTO students (student_id, student_name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Carol');

-- Insert data into grades table
INSERT INTO grades (student_id, subject, grade) VALUES
(1, 'Math', 85),
(1, 'Science', 90),
(2, 'Math', 75),
(2, 'Science', 80),
(3, 'Math', 95),
(3, 'Science', 88);


-- Now, suppose we want to find all students who have an average grade above 85. We can use a subquery to achieve this:

SELECT student_id, student_name
FROM students
WHERE student_id IN (
    SELECT student_id
    FROM grades
    GROUP BY student_id
    HAVING AVG(grade) > 85
);

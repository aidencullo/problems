DROP DATABASE IF EXISTS company;
CREATE DATABASE company;
USE company;

-- Create the Departments table
CREATE TABLE departments (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Create the Employees table
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    salary INTEGER,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

-- Insert sample data into Departments
INSERT INTO departments (id, name) VALUES
(1, 'Engineering'),
(2, 'Marketing'),
(3, 'Sales'),
(4, 'HR'),
(5, 'Finance');

-- Insert sample data into Employees
INSERT INTO employees (id, first_name, last_name, salary, department_id) VALUES
(1, 'John', 'Doe', 120000, 1),
(2, 'Jane', 'Smith', 90000, 1),
(3, 'Alice', 'Johnson', 110000, 1),
(4, 'Bob', 'Brown', 85000, 1),
(5, 'Charlie', 'Davis', 95000, 1),
(6, 'David', 'Wilson', 105000, 1),
(7, 'Eve', 'Miller', 130000, 1),
(8, 'Frank', 'Moore', 80000, 1),
(9, 'Grace', 'Taylor', 70000, 1),
(10, 'Hannah', 'Anderson', 95000, 1),
(11, 'Ivy', 'Thomas', 102000, 1),
(12, 'Jack', 'Jackson', 99000, 2),
(13, 'Kara', 'White', 110000, 2),
(14, 'Leo', 'Martin', 115000, 2),
(15, 'Mia', 'Lee', 80000, 2),
(16, 'Nate', 'Harris', 95000, 2),
(17, 'Olivia', 'Clark', 90000, 2),
(18, 'Paul', 'Lewis', 105000, 2),
(19, 'Quinn', 'Walker', 100000, 3),
(20, 'Rachel', 'Young', 98000, 3),
(21, 'Sam', 'King', 90000, 3),
(22, 'Tina', 'Scott', 102000, 3),
(23, 'Ulysses', 'Adams', 105000, 4),
(24, 'Vera', 'Nelson', 98000, 4),
(25, 'Will', 'Carter', 85000, 4),
(26, 'Xena', 'Mitchell', 99000, 4),
(27, 'Yara', 'Perez', 92000, 5),
(28, 'Zane', 'Roberts', 120000, 5),
(29, 'Anna', 'Turner', 115000, 5),
(30, 'Bill', 'Phillips', 95000, 5),
(31, 'Cody', 'Campbell', 110000, 5),
(32, 'Diana', 'Parker', 125000, 5),
(33, 'Eli', 'Evans', 98000, 5),
(34, 'Fiona', 'Morris', 105000, 5),
(35, 'Gabe', 'Baker', 90000, 5),
(36, 'Holly', 'Gonzalez', 95000, 5),
(37, 'Ian', 'Stewart', 102000, 5),
(38, 'Jill', 'Ramirez', 100000, 5),
(39, 'Kurt', 'Foster', 90000, 5),
(40, 'Lana', 'Reed', 105000, 5),
(41, 'Mike', 'Morgan', 98000, 5),
(42, 'Nina', 'Hill', 95000, 5),
(43, 'Oscar', 'Sullivan', 102000, 5),
(44, 'Pam', 'Coleman', 100000, 5),
(45, 'Quincy', 'Barnes', 90000, 5),
(46, 'Rita', 'Ward', 105000, 5),
(47, 'Steve', 'Fisher', 98000, 5),
(48, 'Tara', 'Powell', 95000, 5),
(49, 'Uma', 'Bryant', 102000, 5),
(50, 'Vince', 'Henderson', 100000, 5),
(51, 'Wendy', 'Graham', 90000, 5),
(52, 'Xavier', 'Reyes', 105000, 5),
(53, 'Yvonne', 'Santos', 98000, 5),
(54, 'Zack', 'Dunn', 95000, 5),
(55, 'Aaron', 'Cole', 102000, 5),
(56, 'Bella', 'Bishop', 100000, 5),
(57, 'Chris', 'Wells', 90000, 5),
(58, 'Drew', 'Ferguson', 105000, 5),
(59, 'Ella', 'Gibson', 98000, 5),
(60, 'Finn', 'Hart', 95000, 5),
(61, 'Gina', 'Harrison', 102000, 5),
(62, 'Hank', 'Ingram', 100000, 5),
(63, 'Iris', 'Jensen', 90000, 5),
(64, 'Jake', 'Keller', 105000, 5),
(65, 'Lily', 'Lambert', 98000, 5),
(66, 'Max', 'Mendez', 95000, 5),
(67, 'Nora', 'Nash', 102000, 5),
(68, 'Owen', 'Owens', 100000, 5),
(69, 'Penny', 'Patterson', 90000, 5),
(70, 'Quentin', 'Quinn', 105000, 5),
(71, 'Rose', 'Reynolds', 98000, 5),
(72, 'Sammy', 'Simpson', 95000, 5),
(73, 'Tom', 'Thompson', 102000, 5),
(74, 'Ursula', 'Underwood', 100000, 5),
(75, 'Violet', 'Vaughn', 90000, 5),
(76, 'Willow', 'Walters', 105000, 5),
(77, 'Xander', 'Xu', 98000, 5);

SELECT
COUNT(CASE WHEN salary > 100000 THEN 1 ELSE NULL END) / COUNT(*) AS percentage_over_100k
FROM
employees
GROUP BY
department_id
HAVING
COUNT(*) > 5
ORDER BY
percentage_over_100k DESC;

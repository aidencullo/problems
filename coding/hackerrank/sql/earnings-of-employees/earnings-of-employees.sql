DROP DATABASE IF EXISTS pivot;
		CREATE DATABASE pivot;

		USE pivot;

-- Create Employee table if it doesn't exist (if schema definition is needed)
CREATE TABLE IF NOT EXISTS Employee (
    employee_id INT,
    name VARCHAR(100),
    months INT,
    salary INT
);

-- Insert sample data into Employee table (if required for testing)
INSERT INTO Employee (employee_id, name, months, salary)
VALUES
    (1, 'John', 12, 5000),
    (2, 'Jane', 10, 6000),
    (3, 'Kimberly', 8, 8744);


SELECT
months * salary, COUNT(*) AS earnings
FROM
Employee
GROUP BY
months * salary
ORDER BY
months * salary DESC
LIMIT 1;

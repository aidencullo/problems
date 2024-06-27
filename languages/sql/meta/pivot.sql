DROP DATABASE IF EXISTS pivot;
		CREATE DATABASE pivot;

		USE pivot;


-- Step 1: Create the Sales table
CREATE TABLE IF NOT EXISTS Sales (
    Year INT,
    Quarter VARCHAR(2),
    Revenue DECIMAL(10, 2)
);

-- Step 2: Insert sample data into the Sales table
INSERT INTO Sales (Year, Quarter, Revenue) VALUES
(2021, 'Q1', 1500.00),
(2021, 'Q2', 2000.00),
(2021, 'Q3', 2500.00),
(2021, 'Q4', 3000.00),
(2022, 'Q1', 1600.00),
(2022, 'Q2', 2100.00),
(2022, 'Q3', 2600.00),
(2022, 'Q4', 3100.00),
(2023, 'Q4', 3100.00);

-- Step 3: Pivot the table using conditional aggregation
SELECT 
    Year,
    SUM(CASE WHEN Quarter = 'Q1' THEN Revenue ELSE 0 END) AS Q1,
    SUM(CASE WHEN Quarter = 'Q2' THEN Revenue ELSE 0 END) AS Q2,
    SUM(CASE WHEN Quarter = 'Q3' THEN Revenue ELSE 0 END) AS Q3,
    SUM(CASE WHEN Quarter = 'Q4' THEN Revenue ELSE 0 END) AS Q4
FROM Sales
GROUP BY Year;

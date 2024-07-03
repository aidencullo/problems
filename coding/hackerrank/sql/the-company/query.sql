CREATE DATABASE IF NOT EXISTS TestDB;

USE TestDB;

DROP TABLE IF EXISTS Company;
DROP TABLE IF EXISTS Lead_Manager;
DROP TABLE IF EXISTS Senior_Manager;
DROP TABLE IF EXISTS Manager;
DROP TABLE IF EXISTS Employee;


-- Create Company Table
CREATE TABLE Company (
    company_code VARCHAR(10),
    founder VARCHAR(100)
);

-- Create Lead_Manager Table
CREATE TABLE Lead_Manager (
    lead_manager_code VARCHAR(10),
    company_code VARCHAR(10)
);

-- Create Senior_Manager Table
CREATE TABLE Senior_Manager (
    senior_manager_code VARCHAR(10),
    lead_manager_code VARCHAR(10),
    company_code VARCHAR(10)
);

-- Create Manager Table
CREATE TABLE Manager (
    manager_code VARCHAR(10),
    senior_manager_code VARCHAR(10),
    lead_manager_code VARCHAR(10),
    company_code VARCHAR(10)
);

-- Create Employee Table
CREATE TABLE Employee (
    employee_code VARCHAR(10),
    manager_code VARCHAR(10),
    senior_manager_code VARCHAR(10),
    lead_manager_code VARCHAR(10),
    company_code VARCHAR(10)
);

-- Insert sample data into Company Table
INSERT INTO Company (company_code, founder) VALUES
('C1', 'Monika'),
('C2', 'Samantha');

-- Insert sample data into Lead_Manager Table
INSERT INTO Lead_Manager (lead_manager_code, company_code) VALUES
('LM1', 'C1'),
('LM2', 'C2');

-- Insert sample data into Senior_Manager Table
INSERT INTO Senior_Manager (senior_manager_code, lead_manager_code, company_code) VALUES
('SM1', 'LM1', 'C1'),
('SM2', 'LM1', 'C1'),
('SM3', 'LM2', 'C2');

-- Insert sample data into Manager Table
INSERT INTO Manager (manager_code, senior_manager_code, lead_manager_code, company_code) VALUES
('M1', 'SM1', 'LM1', 'C1'),
('M2', 'SM3', 'LM2', 'C2'),
('M3', 'SM3', 'LM2', 'C2');

-- Insert sample data into Employee Table
INSERT INTO Employee (employee_code, manager_code, senior_manager_code, lead_manager_code, company_code) VALUES
('E1', 'M1', 'SM1', 'LM1', 'C1'),
('E2', 'M1', 'SM1', 'LM1', 'C1'),
('E3', 'M2', 'SM3', 'LM2', 'C2'),
('E4', 'M3', 'SM3', 'LM2', 'C2');


-- Given the table schemas below, write a query to print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending company_code.


SELECT
c.company_code,
c.founder,
COUNT(DISTINCT e.lead_manager_code) AS total_lead_managers,
COUNT(DISTINCT e.senior_manager_code) AS total_senior_managers,
COUNT(DISTINCT e.manager_code) AS total_managers,
COUNT(DISTINCT e.employee_code) AS total_employees
FROM
Company c
JOIN
Employee e
ON
c.company_code = e.company_code
GROUP BY
c.company_code,
c.founder

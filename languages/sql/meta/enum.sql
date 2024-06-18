DROP DATABASE IF EXISTS test_db;
CREATE DATABASE test_db;
USE test_db;

CREATE TABLE example_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    enum_column ENUM('Value1', 'Value2', 'Value3')
);


INSERT INTO example_table (enum_column) VALUES ('Value1');
INSERT INTO example_table (enum_column) VALUES ('Value2');
INSERT INTO example_table (enum_column) VALUES ('Value3');


SELECT * FROM example_table;

-- Causes an error
-- INSERT INTO example_table (enum_column) VALUES ('Value4');

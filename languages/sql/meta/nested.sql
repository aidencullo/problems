CREATE TABLE data (
    id INT,
    values ARRAY<INT>
);

INSERT INTO data (id, values)
VALUES
    (1, ARRAY[3, 1, 2]),
    (2, ARRAY[5, 4]),
    (3, ARRAY[7, 6, 8]);

SELECT * FROM data;

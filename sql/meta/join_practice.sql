DROP DATABASE IF EXISTS sales_db;
CREATE DATABASE sales_db;
USE sales_db;

CREATE TABLE people(
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100),
  hair_color VARCHAR(100)
);

CREATE TABLE dogs(
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100),
  hair_color VARCHAR(100)
);

INSERT INTO people(name, hair_color)
  VALUES
  ('John', 'brown'),
  ('Jake', 'black'),
  ('Tom', 'black');

INSERT INTO dogs(name, hair_color)
 VALUES
 ('Luna', 'black');

SELECT *
  FROM people
       RIGHT JOIN dogs
		           ON people.hair_color = dogs.hair_color;

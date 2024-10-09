-- # ================================================================ #
-- #                                                                  #
-- # Alfred Santa Molison, 8814921, PROG8850 - Fall 2024 - Section 1  #
-- #                                                                  #
-- # ================================================================ #

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL
);

INSERT INTO departments VALUES (1,'dept_1','Waterloo');
INSERT INTO departments VALUES (2,'dept_2','Kitchener');
INSERT INTO departments VALUES (3,'dept_3','Cambridge');
INSERT INTO departments VALUES (4,'dept_4','Toronto');

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(255) NOT NULL,
    department_id INT,
    location VARCHAR(255) NOT NULL,
    hire_date DATE
);

UPDATE departments
SET department_name = 'new_dept'
WHERE department_id = 1;

DELETE FROM departments
WHERE department_id = 2;
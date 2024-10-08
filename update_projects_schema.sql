-- # ================================================================ #
-- #                                                                  #
-- # Alfred Santa Molison, 8814921, PROG8850 - Fall 2024 - Section 1  #
-- #                                                                  #
-- # ================================================================ #

CREATE TABLE projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    start_date DATE,
    end_date DATE
);

ALTER TABLE projects
ADD COLUMN budget DECIMAL(10, 2);

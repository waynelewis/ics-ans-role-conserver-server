CREATE TABLE Person (
    person_id INT(255) NOT NULL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE Tasks (
    task_id INT(255) NOT NULL PRIMARY KEY,
    subject VARCHAR(50) NOT NULL,
    last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;
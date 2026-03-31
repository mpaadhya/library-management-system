CREATE DATABASE LMS;

USE LMS;

CREATE TABLE books(
book_id INT AUTO_INCREMENT PRIMARY KEY,
book_name VARCHAR(100),
author VARCHAR(100),
pages INT,
book_status INT DEFAULT 0
);

CREATE TABLE member(
member_id INT AUTO_INCREMENT PRIMARY KEY,
member_name VARCHAR(100),
phone VARCHAR(20)
);

CREATE TABLE issue(
issue_id INT AUTO_INCREMENT PRIMARY KEY,
book_id INT,
member_id INT,
issue_date DATE,
return_date DATE
);
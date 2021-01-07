-- create database user and tables --

DROP DATABASE IF EXISTS invoices_db;
CREATE DATABASE IF NOT EXISTS invoices_db;

-- DROP USER IF EXISTS ulter@localhost;
CREATE USER IF NOT EXISTS 'ulter'@'localhost' IDENTIFIED BY 'ulter';
GRANT ALL PRIVILEGES ON `invoices_db`.* TO 'ulter'@'localhost';
FlUSH PRIVILEGES;
-- create a DB
-- name hbbn
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_scheme.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

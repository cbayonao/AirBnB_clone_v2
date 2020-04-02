-- create a DB
-- name hbbn_dev
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY "hbnb_dev_pwd";
GRANT SELECT ON performance_scheme.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY "hbnb_dev_pwd";
FLUSH PRIVILEGES;

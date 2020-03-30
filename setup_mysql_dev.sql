-- create a DB
--name hbbn
CREATE IF NOT EXISTS DATABASE hbhb_dev_db;
CREATE IF NOT EXISTS USER 'hbhb_dev'@'localhost';
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_scheme.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

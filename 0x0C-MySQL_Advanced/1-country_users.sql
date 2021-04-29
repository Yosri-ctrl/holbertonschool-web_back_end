-- create users table
-- containing id, email, name, country
CREATE TABLE IF NOT EXISTS users(
	id int NOT NULL AUTO_INCREMENT,
	email varchar(255) NOT NULL,
	name varchar(255),
	country ENUM('US', 'CO', 'TN') NOT NULL,
	PRIMARY KEY (id)
);

CREATE DATABASE IF NOT EXISTS concessionaria_db;
CREATE TABLE concessionaria_db.carro(
  id_carro INT NOT NULL AUTO_INCREMENT,
  modelo VARCHAR(45) NULL,
  marca VARCHAR(45) NULL,
  PRIMARY KEY (id_carro)
);

CREATE USER 'app_conc_user'@'localhost' IDENTIFIED BY '123';
GRANT ALL PRIVILEGES ON concessionaria_db.* TO 'app_conc_user'@'localhost';

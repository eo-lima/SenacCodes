CREATE DATABASE IF NO EXISTS loja;
USE loja;

CREATE TABLE produtos(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    preco FLOAT NOT NULL,
    quantidade INT NULL,
    garantia INT NULL
);
CREATE DATABASE IF NOT EXISTS cadastro_db CHARACTER SET utf8mb4;

USE cadastro_db;

CREATE TABLE IF NOT EXISTS usuarios(
    id    INT AUTO_INCREMENT PRIMARY KEY,
    nome  VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR (64) NOT NULL
);

insert ignore into usuarios (nome, email, senha) values
('Administrador', 'admin@admin.com', '8c6976e55b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918');
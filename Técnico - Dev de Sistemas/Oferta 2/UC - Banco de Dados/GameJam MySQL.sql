CREATE DATABASE IF NOT EXISTS gamejamdb;
USE gamejamdb;

CREATE TABLE equipe (
    id_equipe INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE participante (
    id_participante INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    curso VARCHAR(100),
    id_equipe INT NOT NULL,
    FOREIGN KEY (id_equipe) REFERENCES equipe(id_equipe)
);

CREATE TABLE jogo (
    id_jogo INT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    genero VARCHAR(50),
    link VARCHAR(200),
    id_equipe INT NOT NULL UNIQUE,
    FOREIGN KEY (id_equipe) REFERENCES equipe(id_equipe)
);

CREATE TABLE jurado (
    id_jurado INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    especialidade VARCHAR(100)
);

CREATE TABLE criterio (
    id_criterio INT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

CREATE TABLE avaliacao (
    id_avaliacao INT PRIMARY KEY,
    nota DECIMAL(3,1) NOT NULL CHECK (nota >= 0 and nota <= 10),
    id_jurado INT NOT NULL,
    id_jogo INT NOT NULL,
    id_criterio INT NOT NULL,
    FOREIGN KEY (id_jurado) REFERENCES jurado(id_jurado),
    FOREIGN KEY (id_jogo) REFERENCES jogo(id_jogo),
    FOREIGN KEY (id_criterio) REFERENCES criterio(id_criterio)
);

INSERT INTO equipe VALUES
(1,'Senac'),(2,'UCDB'),(3,'UFMS');

INSERT INTO participante VALUES
(1,'Enzo Lima','enzo@email.com','Software',1),
(2,'Pedro Menani','pedro@email.com','Software',2),
(3,'Maurício Estevam','mauricio@email.com','Jogos',3);

INSERT INTO jogo VALUES
(1,'Senac Game','Aventura','http://jogos.com/senac',1),
(2,'UCDB Game','Puzzle','http://jogos.com/ucdb',2),
(3,'UFMS Game','RPG','http://jogos.com/ufms',3);

INSERT INTO jurado VALUES
(1,'Prof. Ederson','Programação'),
(2,'Prof. Calebe','Design'),
(3,'Profa. Enilda','Design');

INSERT INTO criterio VALUES 
(1,'Jogabilidade'),(2,'Arte'),(3,'Criatividade');

INSERT INTO avaliacao VALUES
(1, 8.0, 1, 1, 1),
(2, 8.0, 2, 2, 1),
(3, 9.0, 3, 3, 1);

SELECT j.titulo AS jogo, a.nota AS nota FROM avaliacao a JOIN jogo j ON j.id_jogo = a.id_jogo;

UPDATE participante
SET nome = 'Pedrão'
WHERE id_participante = 2;

SELECT * FROM participante;

DELETE FROM avaliacao
WHERE id_avaliacao = 1;
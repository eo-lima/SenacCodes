-- Aluno Enzo Nogueira de Lima
-- UC 07 - Trilha Certa

-- PARTE 1

CREATE DATABASE IF NOT EXISTS trilha_certa;
USE trilha_certa;

CREATE TABLE cliente (
	cod_cliente INT PRIMARY KEY	NOT NULL UNIQUE,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    telefone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NULL
);

CREATE TABLE equipamento (
	cod_equipamento INT PRIMARY KEY NOT NULL UNIQUE,
    nome VARCHAR(100) NOT NULL,
    marca VARCHAR(100) NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    valor_diaria DECIMAL(10,2) NOT NULL CHECK (valor_diaria > 0),
    status VARCHAR(20) NOT NULL DEFAULT 'disponivel' CHECK (status IN ('disponivel', 'alugado', 'manutencao'))
);

CREATE INDEX idx_equipamento_status ON equipamento(status);

CREATE TABLE locacao (
	cod_locacao INT PRIMARY KEY NOT NULL UNIQUE,
    cod_cliente INT NOT NULL,
    data_retirada DATE NOT NULL,
    data_devolucao_prevista DATE NOT NULL CHECK (data_devolucao_prevista >= data_retirada),
    data_devolucao_real DATE NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'aberta' CHECK (status IN ('aberta', 'concluida')),
    FOREIGN KEY (cod_cliente) REFERENCES cliente(cod_cliente)
);

CREATE TABLE item_locacao (
	cod_locacao INT NOT NULL,
    cod_equipamento INT NOT NULL,
    valor_diaria_cobrada DECIMAL (10,2) NOT NULL CHECK (valor_diaria_cobrada > 0),
    PRIMARY KEY (cod_locacao, cod_equipamento),
    FOREIGN KEY (cod_locacao) REFERENCES locacao(cod_locacao),
    FOREIGN KEY (cod_equipamento) REFERENCES equipamento(cod_equipamento)
);

-- PARTE 2

INSERT INTO cliente VALUES 
(1, "Rafaela Mendes", "111.111.111-11", "(67) 99111-0001", "rafaela@email.com"),
(2, "Thiago Barros", "222.222.222-22", "(67) 99222-0002", NULL),
(3, "Camila Nogueira", "333.333.333-33", "(67) 99333-0003", "camila@email.com"),
(4, "Lucas Prado", "444.444.444-44", "(67) 99444-0004", NULL);

INSERT INTO equipamento VALUES 
(101, "Barraca Iglu 3 pessoas", "Quechua", "Barracas", 45, "disponivel"),
(102, "Barraca Cabana 6 pessoas", "Nautika", "Barracas", 70, "alugado"),
(103, "Mochila Cargueira 60L", "Deuter", "Mochilas", 30, "alugado"),
(104, "Fogareiro Portátil Dual", "Mor", "Fogareiros", 20, "manutencao"),
(105, "Lanterna de Cabeça LED", "Petzl", "Iluminação", 12, "alugado"),
(106, "Lampião a Gás", "Coleman", "Iluminação", 18, "disponivel");

INSERT INTO locacao VALUES
(1001, 1, '2026-09-05', '2026-09-08', '2026-09-08', "concluida"),
(1002, 2, '2026-10-02', '2026-10-05', '2026-10-05', "concluida"),
(1003, 3, '2026-10-10', '2026-10-13', NULL, "aberta"),
(1004, 4, '2026-10-17', '2026-10-20', NULL, "aberta");

INSERT INTO item_locacao VALUES
(1001, 101, 45.00),
(1001, 103, 30.00),
(1002, 101, 45.00),
(1002, 106, 18.00),
(1003, 102, 70.00),
(1003, 103, 30.00),
(1004, 105, 12.00);

-- PARTE 3

SELECT nome, marca, valor_diaria FROM equipamento WHERE status = "disponivel" ORDER BY nome;

SELECT nome, telefone FROM cliente WHERE nome LIKE 'C%' OR nome LIKE 'T%' ORDER BY nome;

SELECT nome, valor_diaria FROM equipamento WHERE valor_diaria >= 20 AND valor_diaria <= 45 ORDER BY valor_diaria;

SELECT l.cod_locacao, c.nome AS cliente, l.data_retirada, l.status FROM locacao l INNER JOIN cliente c ON c.cod_cliente = l.cod_cliente ORDER BY l.data_retirada;

SELECT e.nome AS equipamento, l.valor_diaria_cobrada FROM item_locacao l INNER JOIN equipamento e ON e.cod_equipamento = l.cod_equipamento WHERE cod_locacao = 1003 ORDER BY e.nome;

SELECT c.nome AS cliente, e.nome AS equipamento FROM locacao l INNER JOIN cliente c ON c.cod_cliente = l.cod_cliente INNER JOIN item_locacao i ON i.cod_locacao = l.cod_locacao INNER JOIN equipamento e ON e.cod_equipamento = i.cod_equipamento WHERE l.status = "aberta" ORDER BY c.nome, e.nome; 

-- PARTE 4

UPDATE locacao
SET status = "concluida", data_devolucao_real = '2026-10-13'
WHERE cod_locacao = 1003;

UPDATE equipamento
SET status = "disponivel"
WHERE cod_equipamento = 102 OR cod_equipamento = 103;

DELETE FROM equipamento
WHERE cod_equipamento = 104;

-- DELETE FROM cliente
-- WHERE nome = "Rafaela Mendes"; 
-- O banco de dados impediu o delete da Rafaela Mendes, pois ela referencia para a tabela locacao, que não pode ficar sem cliente.
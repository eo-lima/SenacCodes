CREATE TABLE aluno(
	id_aluno INTEGER PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	telefone VARCHAR(11) NOT NULL,
	email VARCHAR(100) NOT NULL
);

CREATE TABLE professor(
	id_professor INTEGER PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	telefone VARCHAR(11) NOT NULL
);

CREATE TABLE instrumento(
	id_instrumento INTEGER PRIMARY KEY,
	nome VARCHAR(100) NOT NULL
);

CREATE TABLE aula(
	id_aula INTEGER PRIMARY KEY,
	id_aluno INTEGER NOT NULL,
	id_professor INTEGER NOT NULL,
	id_instrumento INTEGER NOT NULL,
	data_aula DATE NOT NULL,
	hora_aula TIME NOT NULL,
	status_pagamento BOOLEAN NOT NULL,
	CONSTRAINT fk_aula_aluno FOREIGN KEY (id_aluno) REFERENCES aluno(id_aluno),
	CONSTRAINT fk_aula_professor FOREIGN KEY (id_professor) REFERENCES professor(id_professor),
	CONSTRAINT fk_aula_instrumento FOREIGN KEY (id_instrumento) REFERENCES instrumento(id_instrumento)
);

CREATE TABLE professor_instrumento(
	id_professor INTEGER NOT NULL,
	id_instrumento INTEGER NOT NULL,
	valor_aula NUMERIC(4,2) NOT NULL,

	CONSTRAINT pk_professor_instrumento PRIMARY KEY (id_professor, id_instrumento),
	CONSTRAINT fk_professor_instrumento_professor FOREIGN KEY (id_professor) REFERENCES professor(id_professor),
	CONSTRAINT fk_professor_instrumento_instrumento FOREIGN KEY (id_instrumento) REFERENCES instrumento(id_instrumento)
)
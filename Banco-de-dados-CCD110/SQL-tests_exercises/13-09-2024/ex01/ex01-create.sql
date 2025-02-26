CREATE SCHEMA ex01;

CREATE TABLE
  ex01.professor (
    id_prof BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY (
      START
      WITH
        1 INCREMENT BY 1
    ),
    nome TEXT NOT NULL,
    rua TEXT NOT NULL,
    cidade TEXT NOT NULL,
    telefone TEXT
  );

CREATE TABLE
  ex01.aluno (
    id_aluno BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY (
      START
      WITH
        1 INCREMENT BY 1
    ),
    nome TEXT NOT NULL,
    rua TEXT NOT NULL,
    cidade TEXT NOT NULL
  );

CREATE TABLE
  ex01.disciplina (
    cod_disc CHAR(6) PRIMARY KEY,
    nome TEXT NOT NULL,
    qtt_aulas_semana INT
  );

CREATE TABLE
  ex01.matricula (
    id_aluno BIGINT REFERENCES ex01.aluno (id_aluno),
    cod_disc TEXT REFERENCES ex01.disciplina (cod_disc),
    ano INT,
    semestre INT,
    nota REAL,
    frequencia REAL,
    PRIMARY KEY (id_aluno, cod_disc, ano, semestre)
  );

CREATE TABLE
  ex01.professor_disciplina (
    id_prof BIGINT REFERENCES ex01.professor (id_prof),
    cod_disc TEXT REFERENCES ex01.disciplina (cod_disc),
    PRIMARY KEY (id_prof, cod_disc)
  );
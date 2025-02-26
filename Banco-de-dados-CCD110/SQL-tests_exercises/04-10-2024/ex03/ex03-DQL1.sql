DROP SCHEMA IF EXISTS exercicio CASCADE;

DROP TABLE IF EXISTS exercicio.professor CASCADE;
DROP TABLE IF EXISTS exercicio.aluno CASCADE;
DROP TABLE IF EXISTS exercicio.disciplina CASCADE;
DROP TABLE IF EXISTS exercicio.matricula CASCADE;
DROP TABLE IF EXISTS exercicio.professor_disciplina CASCADE;

CREATE SCHEMA exercicio;


CREATE TABLE exercicio.professor (
    prof_numero SERIAL PRIMARY KEY,
    prof_nome VARCHAR(50),
    prof_rua VARCHAR(50),
    prof_cidade VARCHAR(50),
    prof_telefone VARCHAR(50)
);

CREATE TABLE exercicio.aluno (
    alu_numero SERIAL PRIMARY KEY,
    alu_nome VARCHAR(50),
    alu_rua VARCHAR(50),
    alu_cidade VARCHAR(50)
);

CREATE TABLE exercicio.disciplina (
    disc_codigo VARCHAR(10) PRIMARY KEY,
    disc_nome VARCHAR(50),
    disc_quant_aulas_semana INTEGER
);

CREATE TABLE exercicio.matricula (
    alu_numero INTEGER,
    disc_codigo VARCHAR(10),
    ano INTEGER,
    semestre INTEGER,
    nota FLOAT,
    frequencia FLOAT,
    PRIMARY KEY (alu_numero, disc_codigo, ano, semestre),
    FOREIGN KEY (alu_numero) REFERENCES exercicio.aluno (alu_numero) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (disc_codigo) REFERENCES exercicio.disciplina (disc_codigo) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE exercicio.professor_disciplina (
    prof_numero INTEGER,
    disc_codigo VARCHAR(10),
    PRIMARY KEY (prof_numero, disc_codigo),
    FOREIGN KEY (prof_numero) REFERENCES exercicio.professor (prof_numero)  ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (disc_codigo) REFERENCES exercicio.disciplina (disc_codigo) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Inserir dados na tabela professor
INSERT INTO exercicio.professor (prof_nome, prof_rua, prof_cidade, prof_telefone)
VALUES 
    ('Marcos Santos', 'Rua Castelo Branco, 10', 'São Bernardo do Campo', '(11) 98987-5252'),
    ('Carlos Silva', 'Avenida Paulista, 1500', 'São Paulo', '(11) 3251-2587'),
    ('Maria Souza', 'Rua da Liberdade, 554', 'Rio de Janeiro', '(21) 2507-8963'),
    ('João Silva', 'Rua das Flores, 875', 'Belo Horizonte', '(31) 3571-4285');

-- Inserir dados na tabela aluno
INSERT INTO exercicio.aluno (alu_nome, alu_rua, alu_cidade) 
VALUES 
    ('Ana Silva', 'Rua X, 15', 'São Paulo'),
    ('Pedro Santos', 'Avenida Y, 30', 'Rio de Janeiro'),
    ('Luisa Oliveira', 'Rua Z, 20', 'Belo Horizonte'),
    ('Carlos Ferreira', 'Rua W, 55', 'Curitiba'),
    ('Maria Almeida', 'Avenida V, 70', 'Porto Alegre');

-- Inserir dados na tabela disciplina
INSERT INTO exercicio.disciplina (disc_codigo, disc_nome, disc_quant_aulas_semana) 
VALUES 
    ('MAT101', 'Matemática Básica', 4),
    ('FIS202', 'Física Aplicada', 3),
    ('QUI303', 'Química Geral', 2),
    ('HIS404', 'História do Brasil', 2),
    ('GEO505', 'Geografia Mundial', 3);

-- Inserir dados na tabela matricula
INSERT INTO exercicio.matricula (alu_numero, disc_codigo, ano, semestre, nota, frequencia) 
VALUES 
    (1, 'MAT101', 2024, 1, 10, 10),
    (1, 'FIS202', 2024, 2, 8, 15),
    (2, 'QUI303', 2024, 1, 7, 15),
    (2, 'HIS404', 2024, 1, 5, 15),
    (3, 'MAT101', 2024, 1, 8, 15),
    (3, 'FIS202', 2024, 1, 9, 15),
    (4, 'MAT101', 2024, 1, 10, 15),
    (4, 'FIS202', 2024, 2, 7, 13),
    (5, 'MAT101', 2024, 1, 6, 15),
    (5, 'FIS202', 2024, 2, 10, 10);

-- Inserir dados na tabela professor_disciplina
INSERT INTO exercicio.professor_disciplina (prof_numero, disc_codigo) 
VALUES 
    (1, 'MAT101'),
    (1, 'FIS202'),
    (3, 'QUI303'),
    (4, 'HIS404'),
    (4, 'GEO505');

SELECT alu_nome
FROM exercicio.aluno
WHERE alu_cidade = 'Porto Alegre';

SELECT alu_nome
FROM exercicio.aluno
WHERE alu_cidade = 'São Paulo' or alu_cidade = 'Rio de Janeiro';

SELECT frequencia
FROM exercicio.matricula
WHERE nota > 9
AND disc_codigo = 'FIS202';

-- O nome e o número dos professores que dão aula da disciplina que tem código MAT101:
SELECT p.prof_nome AS "Nome do Professor", p.prof_numero AS "Número do Professor"
FROM exercicio.professor p
JOIN exercicio.professor_disciplina pd ON p.prof_numero = pd.prof_numero
WHERE pd.disc_codigo = 'MAT101';

-- Os nomes de todos os alunos que cursam a disciplina que tem código MAT101:
SELECT a.alu_nome AS "Nome do Aluno"
FROM exercicio.aluno a
JOIN exercicio.matricula m ON a.alu_numero = m.alu_numero
WHERE m.disc_codigo = 'MAT101';

-- Os nomes de todos os professores que ministram disciplina chamada “Física Aplicada”:
SELECT p.prof_nome AS "Nome do Professor"
FROM exercicio.professor p
JOIN exercicio.professor_disciplina pd ON p.prof_numero = pd.prof_numero
JOIN exercicio.disciplina d ON pd.disc_codigo = d.disc_codigo
WHERE d.disc_nome = 'Física Aplicada';

-- Os nomes de todos os alunos que cursam a disciplina que tem nome “Matemática Básica”
SELECT a.alu_nome AS "Nome do Aluno"
FROM exercicio.aluno a
JOIN exercicio.matricula m ON a.alu_numero = m.alu_numero
JOIN exercicio.disciplina d ON m.disc_codigo = d.disc_codigo
WHERE d.disc_nome = 'Matemática Básica';

-- Os nomes de todos os alunos que têm aula com o professor “João Silva”
SELECT DISTINCT a.alu_nome AS "Nome do Aluno" 
FROM exercicio.aluno a
JOIN exercicio.matricula m ON a.alu_numero = m.alu_numero
JOIN exercicio.professor_disciplina pd ON m.disc_codigo = pd.disc_codigo
JOIN exercicio.professor p ON pd.prof_numero = p.prof_numero
WHERE p.prof_nome = 'João Silva';

-- Os nomes de todos os alunos que têm aula com o professor “Marcos Santos”
SELECT DISTINCT a.alu_nome AS "Nome do Aluno"
FROM exercicio.aluno a
JOIN exercicio.matricula m ON a.alu_numero = m.alu_numero
JOIN exercicio.professor_disciplina pd ON m.disc_codigo = pd.disc_codigo
JOIN exercicio.professor p ON pd.prof_numero = p.prof_numero
WHERE p.prof_nome = 'Marcos Santos';

-- Os nomes de todos os alunos que tiraram nota maior que o aluna “Ana Silva” na disciplina FIS202.
SELECT a.alu_nome
FROM exercicio.aluno a, exercicio.aluno b, exercicio.matricula ma, exercicio.matricula mb
WHERE a.alu_numero = ma.alu_numero
AND a.alu_nome <> 'Ana Silva'
AND b.alu_numero = mb.alu_numero
AND b.alu_nome = 'Ana Silva'
AND ma.disc_codigo = 'FIS202'
AND mb.disc_codigo = 'FIS202'
AND ma.nota > mb.nota;


SELECT a.alu_nome
FROM exercicio.aluno a
JOIN exercicio.matricula m ON a.alu_numero = m.alu_numero
WHERE m.disc_codigo = 'FIS202'
AND m.nota > (
    SELECT m2.nota
    FROM exercicio.aluno a2
    JOIN exercicio.matricula m2 ON a2.alu_numero = m2.alu_numero
    WHERE a2.alu_nome = 'Ana Silva'
    AND m2.disc_codigo = 'FIS202'
);

-- Insira um aluno na tabela Aluno porém não insira nenhuma matrícula.
INSERT INTO exercicio.aluno (alu_nome, alu_rua, alu_cidade) 
VALUES ('João da Silva', 'Rua A, 123', 'São Paulo');

SELECT * FROM exercicio.aluno;

-- Insira um professor na tabela Professor porém não insira nenhum registro ProfessorDisciplina
INSERT INTO exercicio.professor (prof_nome, prof_rua, prof_cidade, prof_telefone)
VALUES ('Juliana Almeida', 'Avenida B, 456', 'Rio de Janeiro', '(21) 99999-8888');

SELECT * FROM exercicio.professor;


-- Exibir os nomes dos professores e o código das disciplinas que eles lecionam. Apresentar null caso eles não estejam lecionando nenhuma (dica: left ou right join)
SELECT p.prof_nome, pd.disc_codigo 
FROM exercicio.professor p
LEFT JOIN exercicio.professor_disciplina pd ON p.prof_numero = pd.prof_numero;

-- Listar todos os alunos e as disciplinas em que estão matriculados, incluindo aqueles alunos que não estão matriculados em nenhuma disciplina
SELECT *
FROM  exercicio.aluno a
LEFT JOIN exercicio.matricula m ON a.alu_numero = m.alu_numero;

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

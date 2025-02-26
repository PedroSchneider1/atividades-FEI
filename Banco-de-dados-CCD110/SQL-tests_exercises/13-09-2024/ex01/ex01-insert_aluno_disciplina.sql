INSERT INTO
  ex01.aluno (nome, rua, cidade)
VALUES
  ('Ana Silva',	'Rua X, 15', 'São Paulo'),
  ('Pedro Santos',	'Avenida Y, 30', 'Rio de Janeiro'),
  ('Luisa Oliveira',	'Rua Z, 20',	'Belo Horizonte'),
  ('Carlos Ferreira',	'Rua W, 55',	'Curitiba'),
  ('Maria Almeida',	'Avenida V, 70',	'Porto Alegre');

INSERT INTO
  ex01.disciplina (cod_disc, nome, qtt_aulas_semana)
VALUES
  ('MAT101', 'Matemática Básica', 4),
  ('FIS202', 'Física Aplicada', 3),
  ('QUI303', 'Química Geral', 2),
  ('HIS404', 'História do Brasil', 2),
  ('GEO505', 'Geografia Mundial', 3);

INSERT INTO
  ex01.matricula (id_aluno, cod_disc, ano, semestre, nota, frequencia)
VALUES
  (1, 'MAT101', 2024, 1, 10, 10),
  (1, 'FIS202', 2024, 2, 8, 15),
  (2, 'QUI303', 2024, 1, 7, 15),
  (2, 'HIS404', 2024, 1, 5, 15),
  (3, 'MAT101', 2024, 1, 8, 15),
  (3, 'FIS202', 2024, 2, 9, 15),
  (4, 'MAT101', 2024, 1, 10, 12),
  (4, 'FIS202', 2024, 2, 7, 13),
  (5, 'MAT101', 2024, 1, 6, 15),
  (5, 'FIS202', 2024, 2, 10, 10);
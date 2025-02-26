-- Os nomes de todos os alunos que tiraram nota maior que o aluna “Ana Silva” na disciplina FIS202 --
SELECT A.nome
	FROM ex01.matricula as M
	CROSS JOIN (
	    SELECT M.nota
	    FROM ex01.disciplina as D
	    NATURAL JOIN ex01.matricula as M
	    INNER JOIN ex01.aluno as A on M.id_aluno = A.id_aluno
	    WHERE D.cod_disc = 'FIS202' AND A.nome = 'Ana Silva'
	) as NotaAna
	INNER JOIN ex01.aluno as A on A.id_aluno = M.id_aluno
	WHERE cod_disc = 'FIS202' AND M.nota > NotaAna.nota

	
-- Realize a seguinte inserção:
	-- Insira um aluno na tabela Aluno porém não insira nenhuma matrícula.
	-- Insira um professor na tabela Professor porém não insira nenhum registro ProfessorDisciplina
INSERT INTO
  ex01.aluno (nome, rua, cidade)
VALUES
  ('Pedro Bala', 'Rua dos Bobos, 12', 'Santos');

INSERT INTO
  ex01.professor (nome, rua, cidade, telefone)
VALUES
  (
    'Plínio Pindorama',
    'Rua dos Lindos, 13',
    'São Berlondon',
    '(11) 98887-5252'
  );

SELECT *
	FROM ex01.professor
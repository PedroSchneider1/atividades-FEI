-- Os nomes de todos os alunos que cursam a disciplina que tem nome “Matemática Básica” --
SELECT A.nome
	FROM ex01.disciplina as D
	INNER JOIN ex01.matricula as M ON D.cod_disc = M.cod_disc
	INNER JOIN ex01.aluno as A on M.id_aluno = A.id_aluno
	WHERE D.nome='Matemática Básica'

-- Os nomes de todos os alunos que têm aula com o professor “João Silva” --
SELECT A.nome
	FROM ex01.professor as P
	NATURAL JOIN ex01.professor_disciplina as PD
	NATURAL JOIN ex01.matricula as M
	INNER JOIN ex01.aluno as A on M.id_aluno = A.id_aluno
	WHERE P.nome='João Silva'

-- Os nomes de todos os alunos que têm aula com o professor “Marcos Santos” --
SELECT DISTINCT (A.nome)
	FROM ex01.professor as P
	NATURAL JOIN ex01.professor_disciplina as PD
	NATURAL JOIN ex01.matricula as M
	INNER JOIN ex01.aluno as A on M.id_aluno = A.id_aluno
	WHERE P.nome='Marcos Santos'
--O nome e o número dos professores que dão aula da disciplina que tem código MAT101--
SELECT id_prof, nome
	FROM ex01.professor as P
	NATURAL JOIN ex01.professor_disciplina as PD
	WHERE pd.cod_disc='MAT101'

--Os nomes de todos os alunos que cursam a disciplina que tem código MAT101--
SELECT nome
	FROM ex01.aluno as A
	NATURAL JOIN ex01.matricula as M
	WHERE m.cod_disc='MAT101'
	
--Os nomes de todos os professores que ministram disciplina chamada “Física Aplicada”--
SELECT P.nome
	FROM ex01.disciplina as D
	INNER JOIN ex01.professor_disciplina as PD ON D.cod_disc = PD.cod_disc
	INNER JOIN ex01.professor as P on PD.id_prof = P.id_prof
	WHERE D.nome='Física Aplicada'
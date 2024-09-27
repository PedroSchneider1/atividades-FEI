-- Exibir os nomes dos professores e o código das disciplinas que eles lecionam. Apresentar null caso eles não estejam lecionando nenhuma (dica: left ou right join) --
SELECT nome, cod_disc
	FROM ex01.professor as P
	LEFT JOIN ex01.professor_disciplina as PD on P.id_prof = PD.id_prof

-- Listar todos os alunos e as disciplinas em que estão matriculados, incluindo aqueles alunos que não estão matriculados em nenhuma disciplina --
SELECT A.nome, cod_disc
	from ex01.aluno as A
	LEFT JOIN ex01.matricula as M on A.id_aluno = M.id_aluno
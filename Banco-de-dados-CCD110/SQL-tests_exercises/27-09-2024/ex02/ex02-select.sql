--Exibir o nome de todos os alunos que moram em “Porto Alegre”--
SELECT nome
	FROM ex01.aluno
	WHERE cidade='Porto Alegre'

--Exibir o nome de todos os alunos que moram em “São Paulo” ou “Rio de Janeiro”--
SELECT nome
	FROM ex01.aluno
	WHERE cidade='São Paulo' OR cidade='Rio de Janeiro'

--Exibir a frequência de todos os alunos que tiraram nota maior que 9 na disciplina com código “FIS202”--
SELECT frequencia
	FROM ex01.matricula
	WHERE nota > 9 AND cod_disc = 'FIS202'
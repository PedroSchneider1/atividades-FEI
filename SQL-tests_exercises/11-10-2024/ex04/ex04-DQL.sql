-- Selecione a média de quantidade de aulas que os professores lecionam. --
SELECT ROUND(AVG(qtt_aulas_semana),1) AS media_aulas_prof
	FROM ex01.disciplina d
	JOIN ex01.professor_disciplina pd ON d.cod_disc = pd.cod_disc;

-- Selecione a quantidade máxima de aulas que cada professor leciona. --
SELECT p.id_prof, p.nome, MAX(qtt_aulas_semana) as max_aulas_prof
	FROM ex01.disciplina d
	JOIN ex01.professor_disciplina pd ON d.cod_disc = pd.cod_disc
	JOIN ex01.professor p ON pd.id_prof = p.id_prof
	GROUP BY p.id_prof, p.nome
	ORDER BY max_aulas_prof DESC;

-- Selecione o nome das disciplinas na qual a média das notas é menor que 7,5
	-- Se não houver nenhuma disciplina com essa média, inserir.
SELECT d.nome, AVG(nota) as media
	FROM ex01.matricula m
	JOIN ex01.disciplina d ON d.cod_disc = m.cod_disc
	GROUP BY 1
	HAVING AVG(nota) < 7.5
	ORDER BY media DESC;

-- Selecione os alunos matriculados na disciplina “MAT101”, mas que não estejam matriculados na “FIS202”
	-- Inserir tais registros se não existirem.
SELECT *
	FROM ex01.matricula m
	WHERE cod_disc IN ('MAT101','FIS202')
	ORDER BY cod_disc, id_aluno;

INSERT INTO
  ex01.matricula
VALUES
  ('6','MAT101', '2024', '2', '10', '2');

SELECT *
	FROM ex01.aluno WHERE id_aluno IN (
		SELECT id_aluno
			FROM ex01.matricula m
			WHERE cod_disc = 'MAT101'
		
			EXCEPT
			
		SELECT id_aluno
			FROM ex01.matricula m
			WHERE cod_disc = 'FIS202'
	);
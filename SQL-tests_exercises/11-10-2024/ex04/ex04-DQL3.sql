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

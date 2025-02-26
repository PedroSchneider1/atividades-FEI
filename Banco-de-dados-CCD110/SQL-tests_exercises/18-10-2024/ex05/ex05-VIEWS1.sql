-- 1. Crie uma visão com todas as disciplinas oferecidas neste ano, constando os nomes das disciplinas, nomes e cidades dos professores responsáveis.
CREATE OR REPLACE VIEW ex01.disciplinas_oferecidas(nome_disciplina, nome_professor, cidade) AS
	SELECT DISTINCT d.nome, p.nome, p.cidade
	FROM ex01.disciplina d
	NATURAL JOIN ex01.professor_disciplina pd
	JOIN ex01.professor p ON pd.id_prof = p.id_prof
	JOIN ex01.matricula m ON pd.cod_disc = m.cod_disc
	WHERE m.ano = 2024

SELECT *
	FROM ex01.disciplinas_oferecidas

-- 1a. A partir da visão criada no exercício 1, mostre todos os nomes dos professores que lecionaram neste ano.
SELECT DISTINCT(nome_professor)
	FROM ex01.disciplinas_oferecidas

-- 1b. A partir da visão criada, mostre os nomes de todos os professores que não moram em São Bernardo do Campo e que ministram alguma disciplina nesse ano.
SELECT DISTINCT(nome_professor)
	FROM ex01.disciplinas_oferecidas
	WHERE cidade <> 'São Bernardo do Campo'
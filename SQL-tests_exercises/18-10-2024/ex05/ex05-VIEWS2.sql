-- 2. Crie uma visão com os dados dos professores (número e nome) e a quantidade total de aulas que ministram.
CREATE OR REPLACE VIEW ex01.dados_prof AS
	SELECT p.id_prof, p.nome, SUM(d.qtt_aulas_semana)
	FROM ex01.professor p
	NATURAL JOIN ex01.professor_disciplina pd
	JOIN ex01.disciplina d ON d.cod_disc = pd.cod_disc
	GROUP BY 1, 2;

SELECT *
	FROM ex01.dados_prof

-- 2a. O que acontece com as visões criadas se atribuirmos a disciplina “Inglês Básico” para o professor Carlos Silva? Quais visões foram afetadas?
-- Criando a disciplina "Inglês Básico"
INSERT INTO ex01.disciplina (cod_disc, nome, qtt_aulas_semana)
	VALUES ('ING606', 'Inglês Básico', 2);

SELECT *
	FROM ex01.disciplina;

-- Assimilando a disciplina ao professor 'Carlos Silva'
INSERT INTO ex01.professor_disciplina (id_prof, cod_disc)
	VALUES (
	(SELECT id_prof
	FROM ex01.professor
	WHERE nome = 'Carlos Silva'),
	(SELECT cod_disc
	FROM ex01.disciplina
	WHERE nome = 'Inglês Básico'))

SELECT *
	FROM ex01.professor_disciplina

-- Verificando as views
SELECT *
	FROM ex01.disciplinas_oferecidas
SELECT *
	FROM ex01.dados_prof

-- 2b. Insira uma matrícula da aluna Ana Silva na disciplina de inglês básico nesse ano. Quais visões foram afetadas?
INSERT INTO ex01.matricula (id_aluno, cod_disc, ano, semestre, nota, frequencia)
	VALUES (
	(SELECT id_aluno
	FROM ex01.aluno
	WHERE nome = 'Ana Silva'),
	(SELECT cod_disc
	FROM ex01.disciplina
	WHERE nome = 'Inglês Básico'),
	2024,
	1,
	10,
	15
	)

SELECT *
	FROM ex01.matricula
	ORDER BY id_aluno ASC, cod_disc ASC, ano ASC, semestre ASC

-- Verificando as views
SELECT *
	FROM ex01.disciplinas_oferecidas
SELECT *
	FROM ex01.dados_prof
--Altere a nota de um aluno em uma disciplina específica.--
UPDATE ex01.matricula SET nota=10 WHERE ex01.matricula.id_aluno=101 and ex01.matricula.cod_disc='FIS202';
SELECT nota FROM ex01.matricula WHERE ex01.matricula.id_aluno=101;

--Adicione um professor e associe pelo menos uma nova disciplina a ele.--
INSERT INTO
  ex01.professor (nome, rua, cidade, telefone)
VALUES
  ('Pedro Bala', 'Rua dos Casas, 101', 'São Bernardo do campo', '(13) 99999-9999');

INSERT INTO
  ex01.professor_disciplina(cod_disc,id_prof)
VALUES
  ('GEO505', 5);

--Remova o professor adicionado--
ALTER TABLE ex01.professor_disciplina ADD CONSTRAINT prof_fk FOREIGN KEY (id_prof) REFERENCES ex01.professor (id_prof) ON DELETE CASCADE;
ALTER TABLE ex01.professor_disciplina ADD CONSTRAINT disc_fk FOREIGN KEY (cod_disc) REFERENCES ex01.ex01.disciplina (cod_disc) ON DELETE CASCADE;
DELETE FROM ex01.professor WHERE nome='Pedro Bala';
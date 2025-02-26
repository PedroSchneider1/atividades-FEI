--O código da disciplina de “Matemática Básica”.--
SELECT cod_disc FROM ex01.disciplina WHERE nome='Matemática Básica';

--A rua do professor “Marcos Santos”--
SELECT rua FROM ex01.professor WHERE nome='Marcos Santos';

--Os números dos professores que dão aula da disciplina que tem código MAT101.--
SELECT id_prof FROM ex01.professor_disciplina WHERE cod_disc='MAT101';
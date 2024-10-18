-- 3. Crie um consulta, delete um professor e execute o comando com o auto commit desabilitado.
-- 3a. Execute um select * from professor e nas visões.
-- 3b. Execute o comando rollback.
-- 3c. Execute um select * from professor  e nas visões novamente.
-- 3d. Verifique o que aconteceu e execute o comando commit ao final.
DELETE FROM ex01.professor WHERE nome = 'Marcos Santos'
	
SELECT *
	FROM ex01.professor
SELECT *
	FROM ex01.dados_prof
SELECT *
	FROM ex01.disciplinas_oferecidas

ROLLBACK;
COMMIT;
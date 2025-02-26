-- -> retorna JSON
-- ->> retorna texto
-- ? verifica se existe uma chave/valor
-- @> contém
-- <@ está contido em

-- a. Exiba os nomes dos produtos e todas as cores disponíveis
SELECT nome, 
	detalhes ->> 'cores_disponiveis' as cores_disponiveis
	FROM jsonsql.produtos
	WHERE detalhes ->> 'cores_disponiveis' IS NOT NULL
	
-- b. Exiba os nomes dos produtos com RAM de 16GB
SELECT nome
	FROM jsonsql.produtos
	WHERE detalhes -> 'especificacoes' ->> 'ram' = '16GB'

-- c. Exiba os nomes dos produtos com garantia de 24 meses
SELECT nome
	FROM jsonsql.produtos
	WHERE detalhes ->> 'garantia_meses' = '24'

-- d. Exiba os nomes dos produtos que incluem Netflix nos apps instalados
SELECT nome
	FROM jsonsql.produtos
	WHERE detalhes -> 'apps_instalados' ? 'Netflix'

-- e. Exibir o nome, processador e RAM dos produtos que possuem o campo processador.
SELECT nome,
	detalhes -> 'especificacoes' ->> 'processador' as processador,
	detalhes -> 'especificacoes' ->> 'ram' as RAM
	FROM jsonsql.produtos
	WHERE detalhes -> 'especificacoes' ? 'processador'
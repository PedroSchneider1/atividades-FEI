-- 1. Um jogador solicitou ao suporte uma lista de todos os seus personagens no jogo.
-- Para atender a esta solicitação, crie uma consulta que mostre todos os personagens associados à conta do jogador (ID = 1), exibindo o nome da conta, ID do personagem, nível atual e a classe escolhida para cada personagem.
SELECT ct.nome_conta, ch.id_char, ch.nivel_char, cl.nome_classe
	FROM db_rotmg.conta ct
	NATURAL JOIN db_rotmg.char ch
	JOIN db_rotmg.classe cl ON ch.id_classe = cl.id_classe
	WHERE ID_jogador = 1
	ORDER BY ch.nivel_char DESC;

-- 2. A equipe de desenvolvimento está realizando um estudo sobre o balanceamento de recompensas nas dungeons mais desafiadoras do jogo.
-- Para isso, precisam de uma lista que mostre os itens mais raros (maior Tier) que podem ser obtidos através de monstros boss em dungeons com dificuldade superior a 7. A lista deve incluir o nome do item, seu tier, o nome do monstro que o dropa e informações sobre a dungeon onde o monstro se encontra.
-- Os resultados devem ser ordenados pelo tier do item, mostrando primeiro os mais raros.
SELECT i.nome_item as Item, i.tier_item as Tier, m.nome_monstro as Drop_por, d.nome_dungeon as Dungeon, d.dificuldade_dungeon as Dificuldade
	FROM db_rotmg.monstro m
	NATURAL JOIN db_rotmg.monstro_dropa_item mdi
	NATURAL JOIN db_rotmg.item i
	JOIN db_rotmg.monstro_boss mb ON m.id_monstro = mb.id_monstro
	JOIN db_rotmg.dungeon d ON mb.id_dungeon = d.id_dungeon
	WHERE d.dificuldade_dungeon > 7
	ORDER BY
	  CASE
	    WHEN i.tier_item = 'UT' THEN 0
	    ELSE CAST(SUBSTRING(i.tier_item FROM 2) AS INTEGER)
	  END DESC;

-- 3. Para um evento especial de premiação no jogo, a equipe precisa identificar os jogadores mais dedicados de cada classe.
-- Crie uma consulta que encontre os personagens de maior nível de cada classe que possuem itens do tipo Especial com o tier mais alto. A consulta deve mostrar o nome da classe, nível do personagem, nome do jogador (conta), nome do item especial e seu tier.
-- Esta informação será usada para premiar os jogadores mais dedicados de cada classe que conseguiram obter itens especiais raros.
SELECT ct.nome_conta as Jogador, ch.nivel_char as Nivel, cl.nome_classe as Classe, i.nome_item as Item, i.tier_item as Tier
	FROM db_rotmg.conta ct
	NATURAL JOIN db_rotmg.char ch
	JOIN db_rotmg.classe cl ON ch.id_classe = cl.id_classe
	JOIN db_rotmg.classe_item cli ON ch.id_char = cli.id_char
	JOIN db_rotmg.item i ON cli.id_item = i.id_item
	LEFT JOIN db_rotmg.especial esp ON i.id_item = esp.id_item
	WHERE ch.nivel_char = (
		SELECT MAX(nivel_char)
		FROM db_rotmg.char
		WHERE id_classe = ch.id_classe
	)
	AND
		esp.efeito_especial IS NOT NULL
	AND
		CAST(SUBSTRING(i.tier_item FROM 2) AS INTEGER) > 10 -- Verifica se o tier está acima de T10
	ORDER BY ch.nivel_char, i.tier_item DESC;

-- 4. A equipe de análise de dados do jogo precisa avaliar o sucesso dos eventos realizados.
-- Para isso, necessitam de um relatório que mostre a participação dos jogadores nos eventos, especificamente focando em quantos monstros de evento cada jogador derrotou e quantos itens especiais conseguiu coletar.
-- O relatório deve incluir apenas jogadores que coletaram pelo menos um item, ordenado pela quantidade de itens coletados em ordem decrescente. Essas informações serão utilizadas para melhorar futuros eventos e seu sistema de recompensas.
SELECT c.nome_conta, COUNT(DISTINCT me.id_monstro) AS monstros_evento_derrotados, COUNT(ch.id_jogador) as Itens_especiais_evento
	FROM db_rotmg.classe_item ci
	NATURAL JOIN db_rotmg.item i
	LEFT JOIN db_rotmg.especial esp ON i.id_item = esp.id_item
	JOIN db_rotmg.char ch ON ci.id_char = ch.id_char
	JOIN db_rotmg.conta c ON ch.id_jogador = c.id_jogador
	JOIN db_rotmg.monstro_dropa_item mdi ON i.id_item = mdi.id_item
	JOIN db_rotmg.monstro m ON mdi.id_monstro = m.id_monstro
	JOIN db_rotmg.Monstro_evento me ON ch.ID_char = me.ID_monstro
	WHERE esp.efeito_especial IS NOT NULL
	GROUP BY 1
	ORDER BY Itens_especiais_evento DESC
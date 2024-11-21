-- Iniciar a transação
BEGIN;

-- Insere dados na tabela db_rotmg.Conta
INSERT INTO db_rotmg.Conta (Nome_conta, Senha_conta, Email_conta) VALUES
('BielXP', 'senha123', 'email1@exemplo.com'),
('Pedrola123', 'senha456', 'email2@exemplo.com'),
('IgaoMotoBoy', 'senha789', 'email3@exemplo.com'),
('RafaelKing', 'senha101', 'email4@exemplo.com'),
('Serjao_foguetes', 'senha112', 'email5@exemplo.com');

-- Insere dados na tabela db_rotmg.Classe
INSERT INTO db_rotmg.Classe (Nome_classe, Descricao, Habilidades_classe) VALUES
('Guerreiro', 'Classe focada em combate corpo a corpo', 'Carrega seu escudo e atordoa os inimigos à frente'),
('Mago', 'Classe especializada em magia ofensiva', 'Lança uma bola de fogo num raio de 20 unidades'),
('Arqueiro', 'Classe com habilidades de longo alcance', 'Atira uma flecha carregada, aumentando seu dano em 10%'),
('Clérigo', 'Classe especializada em cura e suporte', 'Cura todos os jogadores num raio de 25 unidades'),
('Assassino', 'Classe focada em furtividade e dano rápido', 'Fica invisível por um curto período de tempo e carrega seu próximo ataque, aumentando a chance de crítico em 5%');

-- Insere dados na tabela db_rotmg.Char
INSERT INTO db_rotmg.Char (Nivel_char, ID_classe, ID_jogador, Email_conta) VALUES
(18, (SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Guerreiro'), 1, 'email1@exemplo.com'),  	-- Jogador 1 como Guerreiro
(20, (SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Mago'), 1, 'email1@exemplo.com'),  		-- Jogador 1 como Mago
(9,  (SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Mago'), 2, 'email2@exemplo.com'),  		-- Jogador 2 como Mago
(17, (SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Arqueiro'), 3, 'email3@exemplo.com'),  	-- Jogador 3 como Arqueiro
(16, (SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Clérigo'), 1, 'email1@exemplo.com'),  	-- Jogador 3 como Clérigo
(20, (SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Clérigo'), 4, 'email4@exemplo.com'),  	-- Jogador 4 como Clérigo
(19, (SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Assassino'), 5, 'email5@exemplo.com');  	-- Jogador 5 como Assassino

-- Insere dados na tabela db_rotmg.Item
INSERT INTO db_rotmg.Item (ID_item, Tier_item, Nome_item, Trocavel) VALUES
(1, 'UT', 'Poção de Vida', FALSE),
(2, 'UT', 'Poção de Mana', FALSE),
(3, 'UT', 'Poção Grande de Vida', FALSE),
(4, 'UT', 'Poção Grande de Mana', FALSE),
(5, 'T1', 'Escudo de Madeira', TRUE),
(7, 'T2', 'Armadura de Ferro', TRUE),
(8, 'T2', 'Armadura de Malha', TRUE),
(10, 'T3', 'Anel de Ataque', TRUE),
(12, 'T4', 'Anel de Mana', TRUE),
(13, 'T4', 'Anel do Gigante', TRUE),
(15, 'T5', 'Anel Afiado', TRUE),
(16, 'T6', 'Anel dos Ventos Uivantes', TRUE),
(17, 'T7', 'Cajado Mágico', TRUE),
(22, 'T8', 'Cajado Elemental', TRUE),
(25, 'T9', 'Super Arco', TRUE),
(27, 'T10', 'Espadão Mágico', FALSE),
(33, 'T11', 'Tomo Arcano', FALSE),
(34, 'T11', 'Adaga Infernal', FALSE),
(36, 'T12', 'Códex Corrompido', FALSE),
(39, 'T13', 'Cetro dos Deuses', FALSE),
(40, 'T13', 'Escudo Amaldiçoado', FALSE),
(50, 'T13', 'Espada Divina', FALSE);

-- Insere dados na tabela db_rotmg.classe_item
INSERT INTO db_rotmg.classe_item (ID_classe, ID_item, ID_char) VALUES
(
	(SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Guerreiro'),  -- Guerreiro
	(SELECT ID_item FROM db_rotmg.item WHERE Nome_item = 'Espadão Mágico'),   -- Espadão Mágico
	(SELECT ID_char FROM db_rotmg.char WHERE id_char = 1)  -- Guerreiro do jogador 1
),
(
	(SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Guerreiro'),  -- Guerreiro
	(SELECT ID_item FROM db_rotmg.item WHERE Nome_item = 'Escudo de Madeira'),  -- Escudo de Madeira
	(SELECT ID_char FROM db_rotmg.char WHERE id_char = 1)  -- Guerreiro do jogador 1
),
(
	(SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Guerreiro'),  -- Guerreiro
	(SELECT ID_item FROM db_rotmg.item WHERE Nome_item = 'Armadura de Ferro'),  -- Armadura de Ferro
	(SELECT ID_char FROM db_rotmg.char WHERE id_char = 1)  -- Guerreiro do jogador 1
),
(
	(SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Guerreiro'),  -- Guerreiro
	(SELECT ID_item FROM db_rotmg.item WHERE Nome_item = 'Anel do Gigante'),    -- Anel do Gigante
	(SELECT ID_char FROM db_rotmg.char WHERE id_char = 1)  -- Guerreiro do jogador 1
),
(
	(SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Mago'),  -- Mago
	(SELECT ID_item FROM db_rotmg.item WHERE Nome_item = 'Cajado Mágico'),      -- Cajado Mágico
	(SELECT ID_char FROM db_rotmg.char WHERE id_char = 2)  -- Mago do jogador 1
),
(
	(SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Mago'),  -- Mago
	(SELECT ID_item FROM db_rotmg.item WHERE Nome_item = 'Cetro dos Deuses'),   -- Cetro Dos Deuses
	(SELECT ID_char FROM db_rotmg.char WHERE id_char = 2)  -- Mago do jogador 1
),
(
	(SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Mago'),  -- Mago
	(SELECT ID_item FROM db_rotmg.item WHERE Nome_item = 'Armadura de Ferro'),  -- Armadura de Ferro
	(SELECT ID_char FROM db_rotmg.char WHERE id_char = 2)  -- Mago do jogador 1
),
(
	(SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Mago'),  -- Mago
	(SELECT ID_item FROM db_rotmg.item WHERE Nome_item = 'Anel de Mana'),       -- Anel de Mana
	(SELECT ID_char FROM db_rotmg.char WHERE id_char = 2)  -- Mago do jogador 1
),
(
	(SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Clérigo'),  -- Clérigo
	(SELECT ID_item FROM db_rotmg.item WHERE Nome_item = 'Tomo Arcano'),        -- Tomo Arcano
	(SELECT ID_char FROM db_rotmg.char WHERE id_char = 5)  -- Clérigo do jogador 1
),
(
	(SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Clérigo'),  -- Clérigo
	(SELECT ID_item FROM db_rotmg.item WHERE Nome_item = 'Armadura de Malha'),  -- Armadura de Malha
	(SELECT ID_char FROM db_rotmg.char WHERE id_char = 5)  -- Clérigo do jogador 1
),
(
	(SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Clérigo'),  -- Clérigo
	(SELECT ID_item FROM db_rotmg.item WHERE Nome_item = 'Poção de Vida'),      -- Poção de Vida
	(SELECT ID_char FROM db_rotmg.char WHERE id_char = 5)  -- Clérigo do jogador 1
),
(
	(SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Arqueiro'),  -- Arqueiro
	(SELECT ID_item FROM db_rotmg.item WHERE Nome_item = 'Super Arco'),         -- Super Arco
	(SELECT ID_char FROM db_rotmg.char WHERE id_char = 4)  -- Arqueiro do jogador 3
),
(
	(SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Arqueiro'),  -- Arqueiro
	(SELECT ID_item FROM db_rotmg.item WHERE Nome_item = 'Armadura de Malha'),  -- Armadura de Malha
	(SELECT ID_char FROM db_rotmg.char WHERE id_char = 4)  -- Arqueiro do jogador 3
),
(
	(SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Arqueiro'),  -- Arqueiro
	(SELECT ID_item FROM db_rotmg.item WHERE Nome_item = 'Anel Afiado'),       	-- Anel Afiado
	(SELECT ID_char FROM db_rotmg.char WHERE id_char = 4)  -- Arqueiro do jogador 3
),
(
	(SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Assassino'),  -- Assassino
	(SELECT ID_item FROM db_rotmg.item WHERE Nome_item = 'Adaga Infernal'),  	-- Adaga Infernal
	(SELECT ID_char FROM db_rotmg.char WHERE id_char = 7)  -- Assassino do jogador 5
),
(
	(SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Assassino'),  -- Assassino
	(SELECT ID_item FROM db_rotmg.item WHERE Nome_item = 'Armadura de Ferro'),  -- Armadura de Ferro
	(SELECT ID_char FROM db_rotmg.char WHERE id_char = 7)  -- Assassino do jogador 5
),
(
	(SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Assassino'),  -- Assassino
	(SELECT ID_item FROM db_rotmg.item WHERE Nome_item = 'Poção Grande de Vida'),  -- Poção Grande de Vida
	(SELECT ID_char FROM db_rotmg.char WHERE id_char = 7)  -- Assassino do jogador 5
),
(
	(SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Mago'),  -- Mago
	(SELECT ID_item FROM db_rotmg.item WHERE Nome_item = 'Cajado Elemental'),   -- Cajado Elemental
	(SELECT ID_char FROM db_rotmg.char WHERE id_char = 3)  -- Mago do jogador 3
),
(
	(SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Mago'),  -- Mago
	(SELECT ID_item FROM db_rotmg.item WHERE Nome_item = 'Cetro dos Deuses'),   -- Cetro Dos Deuses
	(SELECT ID_char FROM db_rotmg.char WHERE id_char = 3)  -- Mago do jogador 3
),
(
	(SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Clérigo'),  -- Clérigo
	(SELECT ID_item FROM db_rotmg.item WHERE Nome_item = 'Códex Corrompido'),   -- Códex Corrompido
	(SELECT ID_char FROM db_rotmg.char WHERE id_char = 6)  -- Clérigo do jogador 6
),
(
	(SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Clérigo'),  -- Clérigo
	(SELECT ID_item FROM db_rotmg.item WHERE Nome_item = 'Armadura de Malha'),  -- Armadura de Malha
	(SELECT ID_char FROM db_rotmg.char WHERE id_char = 6)  -- Clérigo do jogador 6
),
(
	(SELECT ID_classe FROM db_rotmg.classe WHERE Nome_classe = 'Clérigo'),  -- Clérigo
	(SELECT ID_item FROM db_rotmg.item WHERE Nome_item = 'Poção Grande de Vida'),      -- Poção de Vida
	(SELECT ID_char FROM db_rotmg.char WHERE id_char = 6)  -- Clérigo do jogador 6
);

-- Insere dados na tabela db_rotmg.Monstro
INSERT INTO db_rotmg.Monstro (ID_monstro, XP_monstro_dropa, Nome_monstro, Nivel_monstro, Vida_monstro) VALUES
(1, 50, 'Goblin', 1, 100),
(2, 100, 'Esqueleto', 2, 150),
(3, 200, 'Orc', 3, 250),
(4, 150, 'Lobo', 2, 120),
(5, 400, 'Troll', 4, 350),
(9, 300, 'Dragão', 5, 500),
(12, 500, 'Minotauro', 6, 600),
(16, 1000, 'Mago Louco', 10, 1200),
(18, 1250, 'Demônio Falso', 11, 1666),
(20, 1500, 'Guerreiro do Vazio', 13, 2250),
(30, 2250, 'Oryx', 20, 2500);

-- Insere dados na tabela db_rotmg.monstro_dropa_item
INSERT INTO db_rotmg.monstro_dropa_item (ID_item, ID_monstro) VALUES
(1, 1),  -- Goblin dropa Poção de Vida
(2, 2),  -- Esqueleto dropa Poção de Mana
(1, 3),  -- Orc dropa Poção de Vida
(5, 3),  -- Orc dropa Escudo de Madeira
(17, 9),  -- Dragão dropa Cajado Mágico
(22, 9),  -- Dragão dropa Cajado Elemental
(33, 9), -- Dragão dropa Tomo Arcano
(7, 4),  -- Lobo dropa Armadura de Ferro
(2, 5),  -- Troll dropa Poção de Mana
(25, 5),  -- Troll dropa Super Arco
(27, 12),  -- Minotauro dropa Espadão Mágico
(39, 12), -- Minotauro dropa Cetro dos Deuses
(34, 18), -- Demônio Falso dropa Adaga Infernal
(36, 16), -- Mago Louco dropa Códex Corrompido
(40, 20), -- Guerreiro do Vazio dropa Escudo Amaldiçoado
(50,30); -- Oryx dropa Espada Divina

-- Insere dados na tabela db_rotmg.Monstro_lacaio
INSERT INTO db_rotmg.Monstro_lacaio (Bioma_monstro, ID_monstro) VALUES
('Floresta', 1),  -- Goblin em Floresta
('Caverna', 2),   -- Esqueleto em Caverna
('Planície', 3),  -- Orc em Planície
('Montanha', 5),  -- Dragão em Montanha
('Floresta', 4);  -- Lobo em Floresta

-- Insere dados na tabela db_rotmg.Evento
INSERT INTO db_rotmg.Evento (Nome_evento, Tempo_duracao) VALUES
('Caça aos Lobos', 60),    -- Evento de caça de 60 minutos (1h)
('Festival Arcano', 120), -- Festival de 120 minutos (2h)
('Guerra dos Clãs', 1440),  -- Guerra dos Clãs de 1440 minutos (24h)
('Expedição às Montanhas', 90), -- Expedição de 90 minutos (1h30min)
('Desafio Supremo', 360);  -- Desafio Supremo de 360 minutos (6h)

-- Insere dados na tabela db_rotmg.Monstro_evento
INSERT INTO db_rotmg.Monstro_evento (ID_evento, ID_monstro) VALUES
(
	(SELECT ID_evento FROM db_rotmg.Evento WHERE Nome_evento = 'Caça aos Lobos'),
	4 -- Lobo
),
(
	(SELECT ID_evento FROM db_rotmg.Evento WHERE Nome_evento = 'Caça aos Lobos'),
	1 -- Goblin
),
(
	(SELECT ID_evento FROM db_rotmg.Evento WHERE Nome_evento = 'Festival Arcano'),
	9 -- Dragão
),
(
	(SELECT ID_evento FROM db_rotmg.Evento WHERE Nome_evento = 'Guerra dos Clãs'),
	3 -- Orc
),
(
	(SELECT ID_evento FROM db_rotmg.Evento WHERE Nome_evento = 'Expedição às Montanhas'),
	9 -- Dragão
),
(
	(SELECT ID_evento FROM db_rotmg.Evento WHERE Nome_evento = 'Expedição às Montanhas'),
	5 -- Troll
),
(
	(SELECT ID_evento FROM db_rotmg.Evento WHERE Nome_evento = 'Desafio Supremo'),
	30 -- Oryx
);

-- Insere dados na tabela db_rotmg.Dungeon
INSERT INTO db_rotmg.Dungeon (ID_dungeon, Nome_dungeon, Dificuldade_dungeon) VALUES
(1, 'Cova dos Piratas', 1),
(3, 'Labirinto das Aranhas', 2),
(5, 'Masmorra das Sombras', 3),
(6, 'Caverna das Cinzas', 4),
(9, 'Túmulo do Rei Esqueleto', 5),
(11, 'Fortaleza do Dragão', 6),
(13, 'Cemitério Esquecido', 7),
(17, 'Torre do Mago Enlouquecido', 8),
(20, 'Castelo Infernal', 9),
(21, 'As Fissuras', 13);

-- Insere dados na tabela db_rotmg.Inimigos_dungeon
INSERT INTO db_rotmg.Inimigos_dungeon (ID_inimigo, Nome_inimigo, Vida_inimigo, XP_inimigo_dropa, ID_dungeon) VALUES
(1, 'Pirata', 100, 50, 1),
(3, 'Esqueleto Guerreiro', 150, 100, 5),
(6, 'Aranha Gigante', 200, 150, 3),
(10, 'Lich', 250, 300, 6),
(17, 'Dragão Infernal', 400, 500, 6),
(19, 'Pupilo Corrompido', 550, 400, 17),
(22, 'Espírito de Fogo', 500, 400, 20),
(23, 'Gosma Roxa', 800, 500, 21);

INSERT INTO db_rotmg.Monstro_boss(ID_dungeon, ID_monstro) VALUES
(1, 1), -- Goblin na Cova dos Piratas
(9, 2), -- ESqueleto no Túmulo do Rei Esqueleto
(3, 3), -- Orc no Labirinto das Aranhas
(6, 4), -- Lobo na Caverna das Cinzas
(5, 5), -- Troll na Masmorra das Sombras
(11, 9), -- Dragão na Fortaleza do Dragão
(3, 12), -- Minotauro no Labirinto das Aranhas
(17, 16), -- Mago Louco na Torre do Mago Enlouquecido
(20, 18), -- Demônio Falso no Castelo Infernal
(21, 20); -- Guerreiro do Vazio nas Fissuras

-- Insere dados na tabela db_rotmg.Atributos_char
INSERT INTO db_rotmg.Atributos_char (LIFE, MANA, ATT, DEF, SPD, DEX, WIS, VIT, ID_char) VALUES
(500, 200, 50, 30, 60, 40, 20, 70, 1),  -- Atributos do Guerreiro do jogador 1
(300, 400, 30, 20, 70, 60, 90, 40, 2),  -- Atributos do Mago do jogador 1
(300, 400, 30, 20, 70, 60, 90, 40, 3),  -- Atributos do Mago do jogador 2
(400, 250, 40, 30, 80, 70, 40, 50, 4),  -- Atributos do Arqueiro do jogador 3
(600, 500, 20, 50, 50, 50, 100, 80, 5), -- Atributos do Clérigo do jogador 1
(600, 500, 20, 50, 50, 50, 100, 80, 6), -- Atributos do Clérigo do jogador 4
(450, 100, 60, 20, 90, 80, 30, 60, 7);  -- Atributos do Assassino do jogador 5

-- Insere dados nas tabelas de itens específicos (Anel, Pocao, Arma, Especial, Armadura)
INSERT INTO db_rotmg.Anel (Efeito_anel, ID_item) VALUES
('Aumenta dano físico em 10%', 10), -- Anel de Ataque
('Aumenta regeneração de mana em 15%', 12), -- Anel de Mana
('Aumenta a resistência a dano físico em 20%', 13), -- Anel do Gigante
('Aumenta chance de crítico em 10%', 15), -- Anel Afiado
('Aumenta velocidade de movimento em 5%', 16); -- Anel dos Ventos Uivantes

INSERT INTO db_rotmg.Pocao (Tipo_pocao, ID_item) VALUES
('Vida +1', 1), -- Poção de Vida
('Mana +1', 2), -- Poção de Mana
('Vida +2', 3), -- Poção Grande de Vida
('Mana +2', 4); -- Poção Grande de Mana

INSERT INTO db_rotmg.Arma (Efeito_arma, ID_item) VALUES
('Dano mágico aumenta em 20%', 17), -- Cajado Mágico
('Dano mágico elemental aumenta em 33%; Mana recarrega 15% mais rápido', 22), -- Cajado Elemental
('Chance de crítico 5%; Alcance +10 unidades', 25), -- Super Arco
('Dano extra de 35%; Velocidade de Ataque diminui em 5%', 27), -- Espadão Mágico
('Dano crítico aumenta em 10%; Dano extra de 15%; Velocidade de Ataque aumenta em 10%', 34); -- Adaga Infernal

INSERT INTO db_rotmg.Especial (Efeito_especial, ID_item) VALUES
('Resistência a dano fisico aumenta em 5%; Vida aumenta em 50', 5), -- Escudo de Madeira
('Aumenta a cura realizada em 25%; Aumenta a Mana e a Defesa em 50', 33), -- Tomo Arcano
('Aumenta o dano mágico em 33%; Aumenta a Mana em 100; Aumenta o raio de magia em +10 unidades', 39), -- Cetro dos Deuses
('Para cada personagem curado, uma aura de energia escura é liberada ao seu redor, causando 250+50% da sua WIS como dano mágico; Aumenta a Mana em 250', 36), -- Códex Corrompido
('Resistência a todos os tipos de dano aumenta em 25%; Sua vida aumenta em 15% enquanto usar o escudo; Não pode atacar em até 1.5s após usar sua habilidade', 40); -- Escudo Amaldiçoado

INSERT INTO db_rotmg.Armadura (Efeito_armadura, ID_item) VALUES
('Resistência a dano mágico aumenta em 5%', 7), -- Armadura de Ferro
('Resistência a dano físico aumenta em 5%', 8); -- Armadura de Malha

-- Finalizar a transação
COMMIT;
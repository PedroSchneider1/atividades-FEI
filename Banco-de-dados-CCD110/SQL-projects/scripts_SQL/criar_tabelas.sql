CREATE SCHEMA IF NOT EXISTS db_rotmg;

CREATE TABLE db_rotmg.Conta
(
  ID_jogador SERIAL PRIMARY KEY,
  Nome_conta VARCHAR(255) NOT NULL,
  Senha_conta VARCHAR(255) NOT NULL,
  Email_conta VARCHAR(255) NOT NULL,
  UNIQUE (Nome_conta),
  CONSTRAINT conta_email_unique UNIQUE (ID_jogador, Email_conta)
);

CREATE TABLE db_rotmg.Classe
(
  ID_classe SERIAL PRIMARY KEY,
  Nome_classe VARCHAR(255) NOT NULL,
  Descricao VARCHAR(255) NOT NULL,
  Habilidades_classe VARCHAR(255) NOT NULL
);

CREATE TABLE db_rotmg.Item
(
  ID_item INT PRIMARY KEY,
  Tier_item VARCHAR(3) NOT NULL,
  Nome_item VARCHAR(255) NOT NULL,
  Trocavel BOOLEAN NOT NULL
);

CREATE TABLE db_rotmg.Monstro
(
  ID_monstro INT PRIMARY KEY,
  XP_monstro_dropa INT NOT NULL,
  Nome_monstro VARCHAR(255) NOT NULL,
  Nivel_monstro INT NOT NULL,
  Vida_monstro INT NOT NULL
);

CREATE TABLE db_rotmg.monstro_dropa_item
(
  ID_item INT NOT NULL,
  ID_monstro INT NOT NULL,
  FOREIGN KEY (ID_item) REFERENCES db_rotmg.Item(ID_item),
  FOREIGN KEY (ID_monstro) REFERENCES db_rotmg.Monstro(ID_monstro)
);

CREATE TABLE db_rotmg.Monstro_lacaio
(
  Bioma_monstro VARCHAR(255) NOT NULL,
  ID_monstro INT NOT NULL,
  FOREIGN KEY (ID_monstro) REFERENCES db_rotmg.Monstro(ID_monstro)
);

CREATE TABLE db_rotmg.Evento
(
  ID_evento SERIAL PRIMARY KEY,
  Nome_evento VARCHAR(255) NOT NULL,
  Tempo_duracao INT NOT NULL
);

CREATE TABLE db_rotmg.Dungeon
(
  ID_dungeon SERIAL PRIMARY KEY,
  Nome_dungeon VARCHAR(255) NOT NULL,
  Dificuldade_dungeon INT NOT NULL
);

CREATE TABLE db_rotmg.Inimigos_dungeon
(
  ID_inimigo INT PRIMARY KEY,
  Nome_inimigo VARCHAR(255) NOT NULL,
  Vida_inimigo INT NOT NULL,
  XP_inimigo_dropa INT NOT NULL,
  ID_dungeon INT NOT NULL,
  FOREIGN KEY (ID_dungeon) REFERENCES db_rotmg.Dungeon(ID_dungeon)
);

CREATE TABLE db_rotmg.Char
(
  ID_char SERIAL PRIMARY KEY,
  Nivel_char INT NOT NULL,
  ID_classe INT NOT NULL,
  ID_jogador INT NOT NULL,
  Email_conta VARCHAR(255) NOT NULL,
  FOREIGN KEY (ID_classe) REFERENCES db_rotmg.Classe(ID_classe),
  FOREIGN KEY (ID_jogador, Email_conta) REFERENCES db_rotmg.Conta(ID_jogador, Email_conta)
);

CREATE TABLE db_rotmg.classe_item
(
  ID_classe INT NOT NULL,
  ID_item INT NOT NULL,
  ID_char INT NOT NULL,
  FOREIGN KEY (ID_classe) REFERENCES db_rotmg.Classe(ID_classe),
  FOREIGN KEY (ID_item) REFERENCES db_rotmg.Item(ID_item),
  FOREIGN KEY (ID_char) REFERENCES db_rotmg.Char(ID_char)
);


CREATE TABLE db_rotmg.Atributos_char
(
  LIFE INT NOT NULL,
  MANA INT NOT NULL,
  ATT INT NOT NULL,
  DEF INT NOT NULL,
  SPD INT NOT NULL,
  DEX INT NOT NULL,
  WIS INT NOT NULL,
  VIT INT NOT NULL,
  ID_char INT NOT NULL,
  FOREIGN KEY (ID_char) REFERENCES db_rotmg.Char(ID_char)
);

CREATE TABLE db_rotmg.Anel
(
  Efeito_anel VARCHAR(255) NOT NULL,
  ID_item INT NOT NULL,
  FOREIGN KEY (ID_item) REFERENCES db_rotmg.Item(ID_item)
);

CREATE TABLE db_rotmg.Pocao
(
  Tipo_pocao VARCHAR(15) NOT NULL,
  ID_item INT NOT NULL,
  FOREIGN KEY (ID_item) REFERENCES db_rotmg.Item(ID_item)
);

CREATE TABLE db_rotmg.Arma
(
  Efeito_arma VARCHAR(255) NOT NULL,
  ID_item INT NOT NULL,
  FOREIGN KEY (ID_item) REFERENCES db_rotmg.Item(ID_item)
);

CREATE TABLE db_rotmg.Especial
(
  Efeito_especial VARCHAR(255) NOT NULL,
  ID_item INT NOT NULL,
  FOREIGN KEY (ID_item) REFERENCES db_rotmg.Item(ID_item)
);

CREATE TABLE db_rotmg.Armadura
(
  Efeito_armadura VARCHAR(255) NOT NULL,
  ID_item INT NOT NULL,
  FOREIGN KEY (ID_item) REFERENCES db_rotmg.Item(ID_item)
);

CREATE TABLE db_rotmg.Monstro_evento
(
  ID_evento INT NOT NULL,
  ID_monstro INT NOT NULL,
  FOREIGN KEY (ID_evento) REFERENCES db_rotmg.Evento(ID_evento),
  FOREIGN KEY (ID_monstro) REFERENCES db_rotmg.Monstro(ID_monstro)
);

CREATE TABLE db_rotmg.Monstro_boss
(
  ID_dungeon INT NOT NULL,
  ID_monstro INT NOT NULL,
  FOREIGN KEY (ID_dungeon) REFERENCES db_rotmg.Dungeon(ID_dungeon),
  FOREIGN KEY (ID_monstro) REFERENCES db_rotmg.Monstro(ID_monstro)
);
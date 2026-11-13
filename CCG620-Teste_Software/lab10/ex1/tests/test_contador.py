from contador import contar_palavras


def test_texto_vazio_devolve_dicionario_vazio():
    assert contar_palavras("") == {}


def test_uma_palavra():
    assert contar_palavras("teste") == {"teste": 1}


def test_duas_palavras_diferentes():
    assert contar_palavras("bom dia") == {"bom": 1, "dia": 1}


def test_palavra_repetida_acumula():
    assert contar_palavras("dia a dia") == {"dia": 2, "a": 1}


def test_maiusculas_contam_como_minusculas():
    assert contar_palavras("Dia dia DIA") == {"dia": 3}


def test_pontuacao_final_ignorada():
    assert contar_palavras("fim. Fim!") == {"fim": 2}


def test_pontuacao_nas_duas_bordas_virgula_e_ponto_e_virgula():
    assert contar_palavras(",dia, ;dia;") == {"dia": 2}


def test_dois_pontos_e_interrogacao():
    assert contar_palavras(":dia: ?dia?") == {"dia": 2}


def test_so_pontuacao_devolve_vazio():
    assert contar_palavras("... !") == {}


def test_quebra_de_linha_separa_palavras():
    assert contar_palavras("bom\ndia") == {"bom": 1, "dia": 1}


def test_varios_espacos_nao_criam_itens_vazios():
    assert contar_palavras("bom   dia") == {"bom": 1, "dia": 1}


def test_hifen_interno_faz_parte_da_palavra():
    assert contar_palavras("guarda-chuva") == {"guarda-chuva": 1}
